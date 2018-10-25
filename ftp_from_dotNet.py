import ftplib
import gzip
import os
import urllib
import shutil
import xml.etree.ElementTree as et
from datetime import datetime
import pymssql
import sys


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

tree = et.parse(f'd:\\{file_wo_gz}')
root = tree.getroot()


conn = pymssql.connect('CNET','teamlead','gdleads','TestDB')
cursor = conn.cursor()
count_pmid = 0
count_title = 0
count_articletitle = 0
for medline in root.iter('MedlineCitation'):
    authorList = []
    mHeading_desc = []
    pmid = medline.find('PMID').text #.encode(sys.stdout.encoding, errors='replace')
    for pmid_num in medline.findall('PMID'):
        pmid = pmid_num.text
        count_pmid += 1
    # title = medline.find('Article').find('Journal').find('Title').text
    count_title += 1
    # articleTitle = str(medline.find('Article').find('ArticleTitle').text).encode(sys.stdout.encoding, errors='replace')
    count_articletitle += 1
    # print(pmid)
    print(count_pmid,count_title,count_articletitle)
    

print('Hi')

    
    
    # print(pmid,title,articleTitle,country,link_to_pubmed,dateval_day,dateval_month,dateval_year,dateval,current_date)
conn.commit()
conn.close


