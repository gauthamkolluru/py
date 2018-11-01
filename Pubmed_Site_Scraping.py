from bs4 import BeautifulSoup as bs
import pyodbc
import requests
from datetime import datetime


con_string = "DRIVER={SQL Server};SERVER={CNET};DATABASE={Pharma};UID={teamlead};PWD={gdleads}"
conn = pyodbc.connect(con_string)
cur = conn.cursor()
query_to_not_use_pmid = '''select PMID FROM Pubmed_AbstractInfo'''
query_to_update_table = '''INSERT INTO [Pubmed_AbstractInfo]
           ([PMID]
           ,[Title]
           ,[Abstract]
           ,[SPIDER_PMID]
           ,[CreatedDate])
     VALUES
           ((?)
           ,(?)
           ,(?)
           ,(?)
           ,(?))'''
cur.execute(query_to_not_use_pmid)
not_use_pmid_list = list(cur)
cur.execute("select PubMedID from TblPublicationTitles")
title_pubmeid_list = list(cur)
# print(title_pubmeid_list)
for title_pubmeid in title_pubmeid_list:
      try:
            current_date = datetime.now()
            url = 'https://www.ncbi.nlm.nih.gov/pubmed/?term='
            if title_pubmeid[0]:
                  title_pubmeid[0] = int(title_pubmeid[0])
                  if title_pubmeid[0] not in not_use_pmid_list:
                        url = url + str(title_pubmeid[0])
                        # print(url,'========')
                        response = requests.get(url)
                        # print(url,response.status_code)
                        soup = bs(response.text,'html.parser')
                        abstract_div = soup.find('div',class_='abstr')
                        # print(str(abstract_div))
                        site_pmid = soup.find('dl',class_='rprtid').find('dd').find('span',class_='highlight').string
                        # print(site_pmid)
                        site_title = soup.find('div',class_='rprt abstract').find('h1').string
                        # print(site_title)
                        cur.execute(query_to_update_table,(int(title_pubmeid[0]),site_title,str(abstract_div),site_pmid,current_date))
                        conn.commit()
                        # break
      except Exception as e:
            print('Error in PMID: ',title_pubmeid[0])
conn.commit()
conn.close

