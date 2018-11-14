def baseTables_MasterTables():
    import ftplib
    import gzip
    import os
    import urllib
    import urllib.request
    import shutil
    from datetime import datetime
    import pyodbc
    import sys
    from xml.etree import ElementTree as ET
    import collections
    import traceback
    import ftp_gz_grab_extract
    import all_db_queries
    import xml_BaseTables
    import baseTables_MasterTables

    queries = all_db_queries.all_db_queries()

    select_queries_forBase = queries['seq_b']
    select_queries_forMaster = queries['seq_m']
    insert_queries_forMaster = queries['inq_m']
    update_queries_forMaster = queries['upq']

    current_date = datetime.now()

    con_string = "DRIVER={SQL Server};SERVER={CNET};DATABASE={TestDB};UID={teamlead};PWD={gdleads}"
    conn = pyodbc.connect(con_string)
    cursor = conn.cursor()

    try:
        cursor.execute(select_queries_forBase['PMID'])
        PMID_BaseTables_list = [val[0] for val in cursor]
        for baseTable_PMID in PMID_BaseTables_list:
            try:
                cursor.execute(select_queries_forMaster['PMID_Check'], baseTable_PMID)
                for val in cursor:
                    cur_id_master = val[0]
                cursor.execute(select_queries_forBase['ID_for_insertion'], baseTable_PMID)
                for val in cursor:
                    cur_id_base = val[0]
                if cur_id_master:
                    # update & insert queries
                    cursor.execute(update_queries_forMaster['medlinecitation'],(current_date,cur_id_master, baseTable_PMID))
                    cursor.execute(select_queries_forMaster['abstract_Check'],(cur_id_master))
                    abstract_master_contents = [{'id':val[0],'abstracttext':val[1],'label':val[2],'nlmcategory':val[3]} for val in cursor]
                    cursor.execute(select_queries_forBase['existing_abstracts'], (cur_id_base))
                    abstract_base_contents = [{'id':val[0],'abstracttext':val[1],'label':val[2],'nlmcategory':val[3]} for val in cursor]
                    for abs_base in abstract_base_contents:
                        for abs_master in abstract_master_contents:
                            if (abs_master['abstracttext'] in abs_base['abstracttext']) and (abs_master['abstracttext'] is not abs_base['abstracttext']):
                                cursor.execute(
                                    update_queries_forMaster['abstract_text'],
                                    (
                                        abs_base['abstracttext'],
                                        abs_base['label'],
                                        abs_base['nlmcategory'],
                                        abs_base['id']
                                    )
                                )
                            elif (abs_master['label'] in abs_base['label']) and (abs_master['label'] is not abs_base['label']):
                                cursor.execute(
                                    update_queries_forMaster['abstract_text'],
                                    (
                                        abs_base['abstracttext'],
                                        abs_base['label'],
                                        abs_base['nlmcategory'],
                                        abs_base['id']
                                    )
                                )
                            elif (abs_master['nlmcategory'] in abs_base['nlmcategory']) and (abs_master['nlmcategory'] is not abs_base['nlmcategory']):
                                cursor.execute(
                                    update_queries_forMaster['abstract_text'],
                                    (
                                        abs_base['abstracttext'],
                                        abs_base['label'],
                                        abs_base['nlmcategory'],
                                        abs_base['id']
                                    )
                                )
                            else:
                else:
                    pass
            except Exception as e1:
                print(e1)


    except Exception as e:
        print(e)

