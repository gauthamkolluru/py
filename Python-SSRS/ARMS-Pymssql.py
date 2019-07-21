import pymssql, sqlalchemy
import pandas as pd
from pandasql import *

conn = pymssql.connect('Servername','id','pwd','DB Name')

cursor = conn.cursor()

sql = """ select ID_Audit_AnnouncmentForm,
                                  CIQM.System_Issue,
                                  MIPQ.Code_IPlantQSI,
                                  substring(MIPQ.Code_IPlantQSI,1,1) AS 'QSI'
                                  from tbl_CoreAuditAnnou_Main CAM With (nolock)
                                  JOIN tbl_CoreE51_IBTSPARQSI_Main CIQM With (nolock)
                                  ON CAM.ID_Audit_AnnouncmentForm = CIQM.Report_No
                                  JOIN [dbo].[tbl_Master_InPlantQSI] MIPQ With (nolock) ON CIQM.System_Issue = MIPQ.Code_IPlantQSI
                                  WHERE MIPQ.FL_ISDELETED='N'
                                  AND CAM.[AuditStartDate] >= '2016-01-01' and CAM.[AuditEndDate] <= '2018-01-01' """

df1 = pd.read_sql(sql,conn)

#print(df1.values) #checking the values in the dataframe
#print(df1.columns.values) #checking the columnnames of the database

sql1 = """ select ID_Audit_AnnouncmentForm,
									  CIQM.System_Issue,
									  IQSI.Code_IPIAAssmentQSI,
									  substring(IQSI.Code_IPIAAssmentQSI,1,1) AS 'QSI'
									  from tbl_CoreAuditAnnou_Main CAM With (nolock)
									  JOIN tbl_CoreE51_IBTSPARQSI_Main CIQM With (nolock)
									  ON CAM.ID_Audit_AnnouncmentForm = CIQM.Report_No
									  JOIN [dbo].[tbl_Master_IPIAAssmentQSI] IQSI With (nolock) ON CIQM.System_Issue = IQSI.Code_IPIAAssmentQSI
									  WHERE IQSI.FL_ISDELETED='N'
									  AND CAM.[AuditStartDate] >= '2016-01-01' and CAM.[AuditEndDate] <= '2018-01-01' """

df2 = pd.read_sql(sql1, conn)

conn.close()	#At any given point of time, there can only be one connection to the database

df3 = df1.append(df2)

sql3 = """select QSI, CAST (Count(QSI) AS Decimal(5,2)) AS [Count_of_QSI] from df3
                                  group by QSI"""

df4 = sqldf(sql3)

sql4 = """Select 'Total', SUM(Count_of_QSI) as TotalQSI from df4"""

df5 = sqldf(sql4)

df4 = df4.append(pd.DataFrame(columns=['Count_of_QSI'], dtype=float))
df5 = df5.append(pd.DataFrame(columns=['TotalQSI'], dtype=float))

sql5 = """select QSI, 
                           Case 
                                  WHEN TotalQSI = 0
                                  THEN 0 
                           ELSE CAST(((Count_of_QSI)/((TotalQSI)))*100 AS Decimal(5,2))
                           END AS PercQSI
                     from df4 cross join df5"""

df6 = sqldf(sql5)

print(df6.values) #The final result
