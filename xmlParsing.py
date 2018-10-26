import ftplib
import gzip
import os
import urllib
import shutil
from datetime import datetime
import pymssql
import sys
from xml.etree import ElementTree as ET
import collections
import traceback

# Finding & Downloading the required file from the FTP server

ftp = ftplib.FTP('ftp.ncbi.nlm.nih.gov')
ftp.login()
ftp.cwd('pubmed/updatefiles/')
files = ftp.nlst()
for file in files[::-1]:
    if file.split('.')[-1].lower() == 'gz':
        req_file_name = file
        break
filename = req_file_name
file_wo_gz = filename
file_wo_gz = file_wo_gz.split('.')
file_wo_gz.remove('gz')
file_wo_gz = '.'.join(file_wo_gz)

if os.path.exists(f'd:\\{filename}'):
    pass
else:
    urllib.request.urlretrieve(f'ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/{req_file_name}', f'd:\\{filename}')

if os.path.exists(f'd:\\{file_wo_gz}'):
    pass
else:
    with gzip.open(f'd:\\{filename}','rb') as go:
        with open(f'd:\\{file_wo_gz}','wb') as of:
            shutil.copyfileobj(go,of)


# Processing XML

dom = ET.parse(f'd:\\{file_wo_gz}')
root = dom.getroot()

print(len(root))

my_object = root.findall('PubmedArticle/MedlineCitation')


conn = pymssql.connect('CNET','teamlead','gdleads','TestDB')
cursor = conn.cursor()
insert_query_medlinecitation = '''INSERT INTO Pubmed_Medlinecitation_Gautham
        ([PMID]
        ,[Title]
        ,[JournalTitle]
        ,[JournalCountry]
        ,[LinktoPubmed]
        ,[Pub_day]
        ,[Pub_month]
        ,[Pub_year]
        ,[Pubdate]
        ,[CreatedDate])
    VALUES
        (%s
        ,%s
        ,%s
        ,%s
        ,%s
        ,%s
        ,%s
        ,%s
        ,%s
        ,%s)'''

insert_query_abstractText = '''INSERT INTO [Pubmed_Abstracttext_Gautham]
           ([Medlinecitation_id]
           ,[abstracttext]
           ,[label]
           ,[nlmcategory]
           ,[CreatedDate])
     VALUES
           (%s
           ,%s
           ,%s
           ,%s
           ,%s)'''

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

insert_query_meshheading = '''INSERT INTO [Pubmed_meshheading_Gautham]
           ([Medlinecitation_id]
           ,[descriptorname]
           ,[majortopicyn]
           ,[meshheading]
           ,[type]
           ,[ui]
           ,[CreatedDate])
     VALUES
           (%s
           ,%s
           ,%s
           ,%s
           ,%s
           ,%s
           ,%s)'''

try:

    for my_obj in my_object:
        pmid = my_obj.find('PMID').text
        dateval_year = my_obj.find('DateRevised/Year').text
        dateval_month = my_obj.find('DateRevised/Month').text
        dateval_day = my_obj.find('DateRevised/Day').text
        dateval = datetime(int(dateval_year),int(dateval_month),int(dateval_day))
        dateval = dateval.strftime('%d/%m/%Y')
        title = my_obj.find('Article/Journal/Title').text
        articleTitle = my_obj.find('Article/ArticleTitle').text
        abs_txt = my_obj.findall('Article/Abstract/AbstractText')
        abstract_list = []
        if abs_txt :
            for abstract in abs_txt:
                abstract_list.append({'AbstractText':abstract.text, 'Label':abstract.get('Label'), 'NlmCategory':abstract.get('NlmCategory')})
        authors = my_obj.findall('Article/AuthorList/Author')
        author_list = []
        if authors:
            for author in authors:
                if author.find('LastName') or author.find('ForeName') or author.find('Initials'):
                    author_list.append({'LastName':author.find('LastName').text,'ForeName':author.find('ForeName').text, 'Initials':author.find('Initials').text, 'Validyn':author.get('Validyn')})
        country = my_obj.find('MedlineJournalInfo/Country').text
        mh_list = my_obj.findall('MeshHeadingList/MeshHeading/DescriptorName')
        mh_obj = []
        if mh_list:
            for mh in mh_list:
                mh_obj.append({'DescriptorName':mh.text, 'UI':mh.get('UI'), 'MajorTopicYN':mh.get('MajorTopicYN')})
        link_to_pubmed = f'https://www.ncbi.nlm.nih.gov/pubmed/{pmid}'
        current_date = datetime.now()
        # print(abstract_list)
        # print(author_list)
        # print(mh_obj)
        cursor.execute(insert_query_medlinecitation,(pmid,title,articleTitle,country,link_to_pubmed,dateval_day,dateval_month,dateval_year,dateval,current_date))
        if abstract_list and isinstance(abstract_list, collections.Iterable):
            for item in abstract_list:
                cursor.execute(insert_query_abstractText, (pmid,item['AbstractText'],item['Label'],item['NlmCategory'],current_date))
        if author_list and isinstance(author_list, collections.Iterable):
            for item in author_list:
                cursor.execute(insert_query_author, (pmid,item['ForeName'],item['Initials'],item['LastName'],'Null',item['Validyn'],current_date))
        if mh_obj and isinstance(mh_obj, collections.Iterable):
            for item in mh_obj:
                cursor.execute(insert_query_meshheading, (pmid,item['DescriptorName'],item['MajorTopicYN'],'Null','Null',item['UI'],current_date))
except Exception as e:
    print(e)
    traceback.print_exc()
conn.commit()
conn.close


    


