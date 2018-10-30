from bs4 import BeautifulSoup as bs
import pyodbc

con_string = "DRIVER={SQL Server};SERVER={CNET};DATABASE={Pharma};UID={teamlead};PWD={gdleads}"
conn = pyodbc.connect(con_string)
cur = conn.cursor()
cur.execute("select TOP 10 TITLE,PubMedID from tblinfinata_Publications_230")
title_pubmeid_list = list(cur)
print(len(title_pubmeid_list))