from datetime import datetime
import pyodbc
import sys
from xml.etree import ElementTree as ET
import collections
import traceback
import all_db_queries

def xml_BaseTables(file_wo_gz):
    queries = all_db_queries.all_db_queries()

    select_queries = queries['seq_b']

    insert_queries = queries['inq_b']

    truncate_queries = queries['trq']

    # dom = ET.parse(f'd:\\{file_wo_gz}')
    dom = ET.parse(file_wo_gz)
    root = dom.getroot()

    print('XML Parsing Started!')
    print(datetime.now())

    my_object = root.findall('PubmedArticle/MedlineCitation')

    con_string = "DRIVER={SQL Server};SERVER={CNET};DATABASE={TestDB};UID={teamlead};PWD={gdleads}"
    conn = pyodbc.connect(con_string)
    cursor = conn.cursor()

    cursor.execute(select_queries['ID_to_truncate'])

    data_in_temp_tbls = [int(val[0]) for val in cursor][0]

    print(data_in_temp_tbls)

    # truncate all base tables if data exists if length of 'data_in_temp_tbls' is more than 0
    if data_in_temp_tbls != 0:
        for key in truncate_queries.keys():
            cursor.execute(truncate_queries[key])
        cursor.commit()
    # insert/update the base tables once the tables are truncated
        # cursor.execute(select_queries['existing_pmid'])
        # existing_PMID_list =  [val[0] for val in cursor]
    for my_obj in my_object:

        try:
            pmid = my_obj.find('PMID').text
            if hasattr(my_obj.find('Article/Journal/JournalIssue/PubDate/Year'), 'text'):
                dateval_year = my_obj.find('Article/Journal/JournalIssue/PubDate/Year').text
            else:
                dateval_year = ''
            if hasattr(my_obj.find('Article/Journal/JournalIssue/PubDate/Month'), 'text'):
                dateval_month = my_obj.find('Article/Journal/JournalIssue/PubDate/Month').text
            else:
                dateval_month = ''
            if hasattr(my_obj.find('Article/Journal/JournalIssue/PubDate/Day'), 'text'):
                dateval_day = my_obj.find('Article/Journal/JournalIssue/PubDate/Day').text
            else:
                dateval_day = '01'
            if dateval_year and dateval_month:
                dateval = dateval_day + '/' + dateval_month + '/' + dateval_year
            elif dateval_year and (not dateval_month):
                dateval = dateval_year
            else:
                dateval = ''
            if dateval is '' and hasattr(my_obj.find('Article/Journal/JournalIssue/PubDate/MedlineDate'), 'text'):
                medline_date = my_obj.find('Article/Journal/JournalIssue/PubDate/MedlineDate').text
            else:
                medline_date = None
            if hasattr(my_obj.find('Article/Journal/Title'), 'text'):
                title = my_obj.find('Article/Journal/Title').text
            else:
                title = ''
            if hasattr(my_obj.find('Article/ArticleTitle'), 'text'):
                articleTitle = my_obj.find('Article/ArticleTitle').text
            else:
                articleTitle = ''
            abs_txt = my_obj.findall('Article/Abstract/AbstractText')
            abstract_list = []
            if abs_txt:
                for abstract in abs_txt:
                    abstract_list.append({'AbstractText': abstract.text, 'Label': abstract.get(
                        'Label'), 'NlmCategory': abstract.get('NlmCategory')})
            authors = my_obj.findall('Article/AuthorList/Author')
            author_list = []
            if authors:
                for author in authors:
                    Validyn = author.items()[0][1]
                    LastName = ''
                    ForeName = ''
                    Initials = ''
                    for au in author:
                        if au.tag == 'LastName':
                            LastName = au.text.encode(
                                sys.stdout.encoding, errors='replace')
                        if au.tag == 'ForeName':
                            ForeName = au.text.encode(
                                sys.stdout.encoding, errors='replace')
                        if au.tag == 'Initials':
                            Initials = au.text.encode(
                                sys.stdout.encoding, errors='replace')
                    author_list.append(
                        {'LastName': LastName, 'ForeName': ForeName, 'Initials': Initials, 'Validyn': Validyn})
            if hasattr(my_obj.find('MedlineJournalInfo/Country'), 'text'):
                country = my_obj.find('MedlineJournalInfo/Country').text
            else:
                country = ''
            mh_list = my_obj.findall('MeshHeadingList/MeshHeading/DescriptorName')
            mh_obj = []
            if mh_list:
                for mh in mh_list:
                    mh_obj.append({'DescriptorName': mh.text, 'UI': mh.get(
                        'UI'), 'MajorTopicYN': mh.get('MajorTopicYN')})
            link_to_pubmed = f'https://www.ncbi.nlm.nih.gov/pubmed/{pmid}'
            current_date = datetime.now()
            cursor.execute(insert_queries['medlinecitation'], (pmid, title, articleTitle, country, link_to_pubmed,
                                                               dateval_day, dateval_month, dateval_year, dateval,
                                                               current_date, medline_date))
            cursor.execute(select_queries['ID_for_insertion'], pmid)
            ID = [val[0] for val in cursor][0]
            if abstract_list and isinstance(abstract_list, collections.Iterable):
                for item in abstract_list:
                    if item['AbstractText']:
                        cursor.execute(insert_queries['abstractText'], (
                            ID, item['AbstractText'], item['Label'], item['NlmCategory'], current_date))
            if author_list and isinstance(author_list, collections.Iterable):
                for item in author_list:
                    cursor.execute(insert_queries['author'], (
                        ID, item['ForeName'], item['Initials'], item['LastName'], 'Null', item['Validyn'],
                        current_date))
            if mh_obj and isinstance(mh_obj, collections.Iterable):
                for item in mh_obj:
                    if item['DescriptorName']:
                        cursor.execute(insert_queries['meshheading'], (
                            ID, item['DescriptorName'], item['MajorTopicYN'], 'Null', 'Null', item['UI'],
                            current_date))
            conn.commit()
        except Exception as e:
            print(e)
            traceback.print_exc()
            with open(r'C:\Users\skolluru\Desktop\errorlog.txt','a') as el:
                el.write(str(traceback.print_exc()))


    conn.commit()
    conn.close

    print('XML Parsing Completed', datetime.now())
    return 0