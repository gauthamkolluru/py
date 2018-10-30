from bs4 import BeautifulSoup as bs
import pyodbc
import requests


con_string = "DRIVER={SQL Server};SERVER={CNET};DATABASE={Pharma};UID={teamlead};PWD={gdleads}"
conn = pyodbc.connect(con_string)
cur = conn.cursor()
cur.execute("select TOP 10 PubMedID,TITLE from tblinfinata_Publications_230")
title_pubmeid_list = list(cur)
# print(title_pubmeid_list)
for title_pubmeid in title_pubmeid_list:
    url = 'https://www.ncbi.nlm.nih.gov/pubmed/?term='
    if title_pubmeid[0]:
        url = url + str(int(title_pubmeid[0]))
        # print(url)
    else:
        url = url + title_pubmeid[1].replace(' ','+')
        # print(url)
    response = requests.get(url)
    # print(url,response.status_code)
    soup = bs(response.text,'html.parser')
    abstrs = soup.find_all('div')
    for abst in abstrs:
        print(abst['class'])
        break

