# encoding: utf-8
from bs4 import BeautifulSoup, NavigableString
import urllib2 as urllib
import re
import unicodedata
import pandas as pd
import csv
from datetime import date

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}

final_data = []
key_words = ["expect to initiate", "plan to initiate", "initiate phase", "plans to initiate", "intend to initiate",
             "planning to initiate", "we plan to commence", "we plan to advance", "the company expects to initiate",
             "plan to conduct", "we anticipate initiating", "we intend to file", "we expect to begin",
             "is planned to begin", "we plan to design", "we are exploring the expansion", "is planned to initiate",
             "is expected to initiate", "is expected to begin", "will initiate", "we plan on conducting",
             "we intend to advance", "we expect to commence", "will move into the dose expansion", "plans to advance",
             "is planned to commence", "is expected to enroll", "announced plans for", "intent to initiate",
             "intends to initiate", "we anticipate commencing", "is expected to commence", "we intend to conduct",
             "Filing an IND", "we expect to report", "we expect to receive", "we expect to receive data",
             "we plan to submit", "initiate enrollment", "we expect to present", "targeting the initiation",
             "expect to submit an NDA", "preparing to submit an MAA", "planned initiation", "expect to submit",
             "be ready to submit an NDA", "is expected to be initiated"]

data = pd.read_csv("C:\\Users\\skolluru\\Desktop\\report.csv")

final_result = []
print data
for d, row in data.iterrows():
    url = row['URL']
    ticker = row['Ticker']
    filing_date = row['FilingDate']
    exhibit_type = row['Type']
    try:
        if url and isinstance(url, str) and len(url) > 3:
            print(url)
            try:
                with open("C:\\Users\\skolluru\\Desktop\\html_content.txt", "w") as textFile:
                    textFile.close()
            except:
                pass
            request = urllib.Request(url, headers=header)
            url_open = urllib.urlopen(request)
            html_source = url_open.read()
            # print(type(html_source))
            with open('C:\\Users\\skolluru\\Desktop\\html_content.txt', 'wb') as file:
                file.write(html_source)
            # break
            with open('C:\\Users\\skolluru\\Desktop\\html_content.txt', 'r') as page:
                soup = BeautifulSoup(page, "lxml")
            for key in key_words:
                extracted_content = ''
                tags = soup.find_all(string=re.compile(r'\b%s\b' % key, re.I))
                if tags:
                    count = 0
                    tags = list(set(tags))
                    for tag in tags:
                        count += 1
                        extracted_content = ''
                        tag_parent = tag.findParent("p")

                        if isinstance(tag_parent, NavigableString):
                            tag_parent = tag
                        if tag.parent.findParent("table"):
                            tag_parent = False
                        if len(str(tag_parent)) > 20000:
                            tag_parent = False
                        if not tag_parent:
                            tag_parent = tag.findParent("dd")
                            if not tag_parent or len(str(tag_parent)) > 20000:
                                tag_parent = tag.findParent("td")
                                if not tag_parent or len(str(tag_parent)) > 20000:
                                    tag_parent = tag.findParent("th")
                                    if not tag_parent or len(str(tag_parent)) > 20000:
                                        tag_parent = tag.findParent("div")
                        if not tag_parent:
                            tag_parent = tag
                        if tag_parent:
                            if isinstance(tag_parent, NavigableString):
                                content = tag_parent
                            else:
                                content = tag_parent.get_text()
                            if content:
                                content = content.strip()
                                extracted_content = unicodedata.normalize("NFKD", content)
                                extracted_content = extracted_content.encode('ascii', 'ignore').decode('ascii')
                                extracted_content = extracted_content.replace("\n", ' ')
                                extracted_content = extracted_content.replace("\t", ' ')
                                extracted_content = extracted_content.replace(",", '')
                                extracted_content = extracted_content.strip()
                                current_date = date.today()
                                current_date = current_date.strftime("%d-%m-%y")
                                sentence_data = dict()
                                sentence_data['Ticker'] = row['Ticker']
                                sentence_data['FilingDate'] = row['FilingDate']
                                sentence_data['Phrase'] = key
                                sentence_data['Sentence'] = str(extracted_content)  # .strip('\n')
                                sentence_split_list = sentence_data['Sentence'].split('.')
                                for sentence_split in sentence_split_list:
                                    sentence_split = sentence_split.strip()
                                    if sentence_data['Phrase'].upper() in sentence_split.upper():
                                        sentence_data['Sentence'] = sentence_split
                                sentence_data['RecordDate'] = current_date
                                sentence_data['Type'] = exhibit_type
                                final_result.append(sentence_data)
                                print "final"

    except Exception as e:
        print(e, "Exception Occured")
        pass
    print len(final_result)
    # if len(final_result) > 900:
    #     break

if len(final_result) > 0:
    file_path = "C:\\Users\\skolluru\\Desktop\\report_gautham.csv"
    with open(file_path, "wb") as csvFile:
        con = csv.DictWriter(csvFile, fieldnames=['Ticker', 'FilingDate', 'Phrase', 'Sentence', 'RecordDate', 'Type'])
        con.writeheader()
        for data in final_result:
            con.writerow(data)
