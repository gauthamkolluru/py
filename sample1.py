import os
import shutil
from datetime import datetime
import sys
from xml.etree import ElementTree as ET
import collections
import traceback
import codecs
import pymssql

conn = pymssql.connect('CNET','teamlead','gdleads','TestDB')
cursor = conn.cursor()


dom = ET.parse('d:\\pubmed18n1306.xml')
root = dom.getroot()

print(len(root))

my_object = root.findall('PubmedArticle/MedlineCitation')
count =0
current_date = datetime.now()
insert_query_author = '''INSERT INTO [Pubmed_author_Gautham]
           ([Medlinecitation_id]
           ,[authfore]
           ,[authinit]
           ,[authlast]
           ,[author]
           ,[validyn]
           ,[CreatedDate])
     VALUES
           (%s
           ,%s
           ,%s
           ,%s
           ,%s
           ,%s
           ,%s)'''
for my_obj in my_object:
    my_authors = my_obj.findall('Article/AuthorList/Author')
    # print(len(my_authors))
    author_list = []
    for my_author in my_authors:
        Validyn = my_author.get('Validyn')
        LastName = ''
        ForeName = ''
        Initials = ''
        for i in my_author:
            print(i)
            # if i.tag == 'LastName':
            #     LastName = i.text.encode(sys.stdout.encoding, errors='replace')
            # if i.tag == 'ForeName':
            #     ForeName = i.text.encode(sys.stdout.encoding, errors='replace')
            # if i.tag == 'Initials':
            #     Initials = i.text.encode(sys.stdout.encoding, errors='replace')
            # author_list.append({'LastName':LastName,'ForeName':ForeName, 'Initials':Initials, 'Validyn':Validyn})
    # if author_list and isinstance(author_list, collections.Iterable):
    #         for item in author_list:
    #             cursor.execute(insert_query_author, (1,item['ForeName'],item['Initials'],item['LastName'],'Null',item['Validyn'],current_date))
    #             conn.commit()
        
conn.commit()
conn.close
