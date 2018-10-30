import os
import shutil
from datetime import datetime
import sys
from xml.etree import ElementTree as ET
import collections
import traceback
import codecs
import pyodbc

# con_string = "DRIVER={SQL Server};SERVER={CNET};DATABASE={TestDB};UID={teamlead};PWD={gdleads}"
# conn = pyodbc.connect(con_string)
# cursor = conn.cursor()


dom = ET.parse('d:\\pubmed18n1306.xml')
root = dom.getroot()

print(len(root))

my_object = root.findall('PubmedArticle/MedlineCitation')
count = 0
current_date = datetime.now()
# insert_query_author = '''INSERT INTO [Pubmed_author_Gautham]
#            ([Medlinecitation_id]
#            ,[authfore]
#            ,[authinit]
#            ,[authlast]
#            ,[author]
#            ,[validyn]
#            ,[CreatedDate])
#      VALUES
#            ((?)
#            ,(?)
#            ,(?)
#            ,(?)
#            ,(?)
#            ,(?)
#            ,(?))'''
for my_obj in my_object:
    # if hasattr(my_obj.find('Article/Journal/JournalIssue/PubDate/Day'),'text'):
    #     print('hi')
    if hasattr(my_obj.find('Article/Journal/JournalIssue/PubDate/Year'),'text'):
        dateval_year = my_obj.find('Article/Journal/JournalIssue/PubDate/Year').text
    else:
        dateval_year = ''
    if hasattr(my_obj.find('Article/Journal/JournalIssue/PubDate/Month'),'text'):
        dateval_month = my_obj.find('Article/Journal/JournalIssue/PubDate/Month').text
    else:
        dateval_month = ''
    if hasattr(my_obj.find('Article/Journal/JournalIssue/PubDate/Day'),'text'):
        dateval_day = my_obj.find('Article/Journal/JournalIssue/PubDate/Day').text
    else:
        dateval_day = '01'
    if dateval_year and dateval_month:
        dateval = dateval_day+'/'+dateval_month+'/'+dateval_year
    else:
        dateval = ''
    if dateval is '' and hasattr(my_obj.find('Article/Journal/JournalIssue/PubDate/MedlineDate'),'text'):
        medline_date = my_obj.find('Article/Journal/JournalIssue/PubDate/MedlineDate').text
    else:
        medline_date = None
    print('dateval = ',dateval)
    print('medline_date = ',medline_date)

        
# conn.commit()
# conn.close
