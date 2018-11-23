from datetime import datetime
import pyodbc
import all_db_queries
import traceback


def baseTables_MasterTables():
    queries = all_db_queries.all_db_queries()

    select_queries_forBase = queries['seq_b']
    select_queries_forMaster = queries['seq_m']
    insert_queries_forMaster = queries['inq_m']
    update_queries_forMaster = queries['upq']

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    con_string = "DRIVER={SQL Server};SERVER={CNET};DATABASE={TestDB};UID={teamlead};PWD={gdleads}"
    conn = pyodbc.connect(con_string)
    cursor = conn.cursor()

    try:
        print(datetime.now())
        cursor.execute('''SELECT PMID FROM Pubmed_Medlinecitation''')
        PMID_BaseTables_list = [int(val[0]) for val in cursor]
        print('PMID_BaseTables_list : ', PMID_BaseTables_list)
        # print(PMID_BaseTables_list)
        # exit(1)
        for baseTable_PMID in PMID_BaseTables_list:
            try:
                cursor.execute('''SELECT ID FROM Pubmed_Master_Medlinecitation where PMID = (?)''', (baseTable_PMID))
                cur_id_master = [int(val[0]) for val in cursor]
                if cur_id_master:
                    cur_id_master = cur_id_master[0]
                print('cur_id_master : ',cur_id_master)
                # exit(1)
                cursor.execute(select_queries_forBase['ID_for_insertion'], baseTable_PMID)
                for val in cursor:
                    cur_id_base = val[0]
                if cur_id_master:
                    # update & insert queries
                    cursor.execute('''UPDATE [Pubmed_Master_Medlinecitation] SET [ModifiedDate] = (?) 
                                        WHERE ID = (?)''',
                                   (current_date, cur_id_master))
                    cursor.commit()

                    # Checking for Abstracts

                    cursor.execute(select_queries_forMaster['abstract_Check'], (cur_id_master))
                    abstract_master_contents = [
                        {'id': val[0], 'abstracttext': val[1], 'label': val[2], 'nlmcategory': val[3]} for val in
                        cursor]

                    print('abstract_master_contents: ',abstract_master_contents)
                    cursor.execute(select_queries_forBase['existing_abstracts'], (cur_id_base))
                    abstract_base_contents = [
                        {'id': val[0], 'abstracttext': val[1], 'label': val[2], 'nlmcategory': val[3]} for val in
                        cursor]
                    for abs_base in abstract_base_contents:
                        for abs_master in abstract_master_contents:
                            if (abs_master['abstracttext'] == abs_base['abstracttext']) and (
                                    abs_master['label'] == abs_base['label']) and (
                                    abs_master['nlmcategory'] == abs_base['nlmcategory']):
                                continue
                            elif ((abs_master['label']) and (abs_base['label'])) and ((abs_base['nlmcategory']) and (abs_master['nlmcategory'])) and ((abs_master['abstracttext'] in abs_base['abstracttext']) or (abs_base['abstracttext'] in abs_master['abstracttext'])) and ((
                                    abs_master['abstracttext'] != abs_base['abstracttext']) or ((
                                    abs_master['label'] != abs_base['label'])) or ((
                                    abs_master['nlmcategory'] != abs_base['nlmcategory']))):
                                cursor.execute(
                                    update_queries_forMaster['abstract_text'],
                                    (
                                        abs_base['abstracttext'],
                                        abs_base['label'],
                                        abs_base['nlmcategory'],
                                        current_date,
                                        abs_master['id']
                                    )
                                )
                                continue
                        else:
                            cursor.execute(
                                insert_queries_forMaster['abstractText'],
                                (
                                    cur_id_master,
                                    abs_base['abstracttext'],
                                    abs_base['label'],
                                    abs_base['nlmcategory'],
                                    current_date,
                                    current_date
                                )
                            )

                    # Checking for Authors

                    cursor.execute(select_queries_forMaster['author_Check'], (cur_id_master))
                    author_master_contents = [
                        {'id': val[0], 'authfore': val[1], 'authinit': val[2], 'authlast': val[3], 'author': val[4],
                         'validyn': [5]} for val in cursor]
                    cursor.execute(select_queries_forBase['existing_authors'], (cur_id_base))
                    author_base_contents = [
                        {'id': val[0], 'authfore': val[1], 'authinit': val[2], 'authlast': val[3], 'author': val[4],
                         'validyn': val[5]} for val in cursor]
                    for abs_base in author_base_contents:
                        for abs_master in author_master_contents:
                            if (abs_master['authfore'] == abs_base['authfore']) and (
                                    abs_master['authinit'] == abs_base['authinit']) and (
                                    abs_master['authlast'] == abs_base['authlast']) and (
                                    abs_master['author'] == abs_base['author']) and (
                                    abs_master['validyn'] == abs_base['validyn']):
                                continue
                            elif (abs_master['authfore']) and (abs_base['authfore']) and (abs_master['authfore'] in abs_base['authfore']) and (
                                    abs_master['authfore'] != abs_base['authfore']):
                                cursor.execute(
                                    update_queries_forMaster['author'],
                                    (
                                        abs_base['authfore'],
                                        abs_base['authinit'],
                                        abs_base['authlast'],
                                        abs_base['author'],
                                        abs_base['validyn'],
                                        current_date,
                                        abs_master['id']
                                    )
                                )
                                continue
                            elif (abs_master['authinit']) and (abs_base['authinit']) and (abs_master['authinit'] in abs_base['authinit']) and (
                                    abs_master['authinit'] != abs_base['authinit']):
                                cursor.execute(
                                    update_queries_forMaster['author'],
                                    (
                                        abs_base['authfore'],
                                        abs_base['authinit'],
                                        abs_base['authlast'],
                                        abs_base['author'],
                                        abs_base['validyn'],
                                        current_date,
                                        abs_master['id']
                                    )
                                )
                                continue
                            elif (abs_master['authlast']) and (abs_base['authlast']) and (abs_master['authlast'] in abs_base['authlast']) and (
                                    abs_master['authlast'] != abs_base['authlast']):
                                cursor.execute(
                                    update_queries_forMaster['author'],
                                    (
                                        abs_base['authfore'],
                                        abs_base['authinit'],
                                        abs_base['authlast'],
                                        abs_base['author'],
                                        abs_base['validyn'],
                                        current_date,
                                        abs_master['id']
                                    )
                                )
                                continue
                            elif (abs_master['author']) and (abs_base['author']) and (abs_master['author'] in abs_base['author']) and (
                                    abs_master['author'] != abs_base['author']):
                                cursor.execute(
                                    update_queries_forMaster['author'],
                                    (
                                        abs_base['authfore'],
                                        abs_base['authinit'],
                                        abs_base['authlast'],
                                        abs_base['author'],
                                        abs_base['validyn'],
                                        current_date,
                                        abs_master['id']
                                    )
                                )
                                continue
                            elif (abs_master['validyn']) and (abs_base['validyn']) and (
                                    abs_master['validyn'] != abs_base['validyn']):
                                cursor.execute(
                                    update_queries_forMaster['author'],
                                    (
                                        abs_base['authfore'],
                                        abs_base['authinit'],
                                        abs_base['authlast'],
                                        abs_base['author'],
                                        abs_base['validyn'],
                                        current_date,
                                        abs_master['id']
                                    )
                                )
                                continue
                        else:
                            cursor.execute(
                                insert_queries_forMaster['author'],
                                (
                                    cur_id_master,
                                    abs_base['authfore'],
                                    abs_base['authinit'],
                                    abs_base['authlast'],
                                    abs_base['author'],
                                    abs_base['validyn'],
                                    current_date,
                                    current_date
                                )
                            )

                    # Checking for Meshheadings
                    cursor.execute(select_queries_forMaster['meshheading_Check'], (cur_id_master))
                    abstract_master_contents = [
                        {'id': val[0] if val[0] else '', 'descriptorname': val[1] if val[1] else '',
                         'majortopicyn': val[2] if val[2] else '', 'meshheading': val[3] if val[3] else '',
                         'type': val[4] if val[4] else '', 'ui': val[5] if val[5] else ''} for val
                        in
                        cursor]
                    cursor.execute(select_queries_forBase['existing_meshheading'], (cur_id_base))
                    abstract_base_contents = [
                        {'id': val[0] if val[0] else '', 'descriptorname': val[1]  if val[1] else '', 'majortopicyn': val[2] if val[2] else '', 'meshheading': val[3] if val[3] else '',
                         'type': val[4] if val[4] else '', 'ui': val[5] if val[5] else ''} for val
                        in
                        cursor]
                    for abs_base in abstract_base_contents:
                        for abs_master in abstract_master_contents:
                            if (abs_master['descriptorname'] == abs_base['descriptorname']) and (
                                    abs_master['majortopicyn'] == abs_base['majortopicyn']) and (
                                    abs_master['meshheading'] == abs_base['meshheading']) and (
                                    abs_master['type'] == abs_base['type']) and (
                                    abs_master['ui'] == abs_base['ui']):
                                continue
                            elif (abs_master['descriptorname']) and (abs_base['descriptorname']) and (abs_master['descriptorname'] in abs_base['descriptorname']) and (
                                    abs_master['descriptorname'] != abs_base['descriptorname']):
                                cursor.execute(
                                    update_queries_forMaster['meshheading'],
                                    (
                                        abs_base['descriptorname'],
                                        abs_base['majortopicyn'],
                                        abs_base['meshheading'],
                                        abs_base['type'],
                                        abs_base['ui'],
                                        current_date,
                                        abs_master['id']
                                    )
                                )
                                continue
                            elif (abs_master['majortopicyn']) and (abs_base['majortopicyn']) and (
                                    abs_master['majortopicyn'] != abs_base['majortopicyn']):
                                cursor.execute(
                                    update_queries_forMaster['meshheading'],
                                    (
                                        abs_base['descriptorname'],
                                        abs_base['majortopicyn'],
                                        abs_base['meshheading'],
                                        abs_base['type'],
                                        abs_base['ui'],
                                        current_date,
                                        abs_base['id']
                                    )
                                )
                                continue
                            elif (abs_master['meshheading']) and (abs_base['meshheading']) and (abs_master['meshheading'] in abs_base['meshheading']) and (
                                    abs_master['meshheading'] != abs_base['meshheading']):
                                cursor.execute(
                                    update_queries_forMaster['meshheading'],
                                    (
                                        abs_base['descriptorname'],
                                        abs_base['majortopicyn'],
                                        abs_base['meshheading'],
                                        abs_base['type'],
                                        abs_base['ui'],
                                        current_date,
                                        abs_master['id']
                                    )
                                )
                                continue
                            elif (abs_master['type']) and (abs_base['type']) and (abs_master['type'] in abs_base['type']) and (
                                    abs_master['type'] != abs_base['type']):
                                cursor.execute(
                                    update_queries_forMaster['meshheading'],
                                    (
                                        abs_base['descriptorname'],
                                        abs_base['majortopicyn'],
                                        abs_base['meshheading'],
                                        abs_base['type'],
                                        abs_base['ui'],
                                        current_date,
                                        abs_master['id']
                                    )
                                )
                                continue
                            elif (abs_master['ui']) and (abs_base['ui']) and (abs_master['ui'] in abs_base['ui']) and (
                                    abs_master['ui'] != abs_base['ui']):
                                cursor.execute(
                                    update_queries_forMaster['meshheading'],
                                    (
                                        abs_base['descriptorname'],
                                        abs_base['majortopicyn'],
                                        abs_base['meshheading'],
                                        abs_base['type'],
                                        abs_base['ui'],
                                        current_date,
                                        abs_master['id']
                                    )
                                )
                                continue
                        else:
                            cursor.execute(
                                insert_queries_forMaster['meshheading'],
                                (
                                    cur_id_master,
                                    abs_base['descriptorname'],
                                    abs_base['majortopicyn'],
                                    abs_base['meshheading'],
                                    abs_base['type'],
                                    abs_base['ui'],
                                    current_date,
                                    current_date
                                )
                            )
                else:
                    print('executing else block')
                    cursor.execute(insert_queries_forMaster['medlinecitation'], baseTable_PMID, cur_id_base)
                    conn.commit()
                    cursor.execute('''SELECT ID FROM Pubmed_Master_Medlinecitation where PMID = (?)''', (baseTable_PMID))
                    id = [int(val[0]) for val in cursor][0]
                    # print(id)
                    cursor.execute('''INSERT INTO Pubmed_Master_Abstracttext (Medlinecitation_id,
                        abstracttext, label, nlmcategory, CreatedDate, ModifiedDate)
                            SELECT	(SELECT
                                        id
                                    FROM Pubmed_Master_Medlinecitation
                                    WHERE PMID = (?)),
                                    abstracttext,
                                    label,
                                    nlmcategory,
                                    CreatedDate,
                                    CreatedDate
                            FROM Pubmed_Abstracttext
                            WHERE Medlinecitation_id = (SELECT
                                Pubmed_Medlinecitation.ID
                            FROM Pubmed_Medlinecitation
                            WHERE PMID = (?))''', (baseTable_PMID, baseTable_PMID))
                    cursor.execute('''INSERT INTO Pubmed_Master_Author (Medlinecitation_id, authfore, authinit, authlast, author, validyn, CreatedDate, ModifiedDate)
                        SELECT	(SELECT
                                    id
                                FROM Pubmed_Master_Medlinecitation
                                WHERE PMID = (?)),
                                authfore,
                                authinit,
                                authlast,
                                author,
                                validyn,
                                CreatedDate,
                                CreatedDate
                        FROM Pubmed_author
                        WHERE Medlinecitation_id = (SELECT
                            Pubmed_Medlinecitation.ID
                        FROM Pubmed_Medlinecitation
                        WHERE PMID = (?))''', (baseTable_PMID,baseTable_PMID))
                    cursor.execute('''INSERT INTO Pubmed_Master_meshheading (Medlinecitation_id, descriptorname, majortopicyn, meshheading, type, ui, CreatedDate, ModifiedDate)
                        SELECT	(SELECT
                                    id
                                FROM Pubmed_Master_Medlinecitation
                                WHERE PMID = (?)),
                                descriptorname,
                                majortopicyn,
                                meshheading,
                                type,
                                ui,
                                CreatedDate,
                                CreatedDate
                        FROM Pubmed_meshheading
                        WHERE Medlinecitation_id = (SELECT
                            Pubmed_Medlinecitation.ID
                        FROM Pubmed_Medlinecitation
                        WHERE PMID = (?))''', (baseTable_PMID, baseTable_PMID))
                    conn.commit()
                    # exit(1)
                    # print(baseTable_PMID)
            except Exception as e1:
                print(e1)
                traceback.print_exc()
                with open(r'C:\Users\skolluru\Desktop\errorlog.txt', 'a') as el:
                    el.write(str(traceback.print_exc()))
    except Exception as e:
        print(e)
        traceback.print_exc()
        with open(r'C:\Users\skolluru\Desktop\errorlog.txt', 'a') as el:
            el.write(str(traceback.print_exc()))

    conn.commit()
    conn.close
    print(datetime.now())
    return 0


# baseTables_MasterTables()