def all_db_queries():
    insert_queries = {'base':{},'master':{}}
    update_queries = {}
    select_queries = {'forBase':{},'forMaster':{}}
    truncate_queries = {}

    insert_queries['base'].update({'medlinecitation': '''INSERT INTO Pubmed_Medlinecitation
                ([PMID]
                ,[Title]
                ,[JournalTitle]
                ,[JournalCountry]
                ,[LinktoPubmed]
                ,[Pub_day]
                ,[Pub_month]
                ,[Pub_year]
                ,[Pubdate]
                ,[CreatedDate]
                ,[MedlineDate])
            VALUES
                ((?)
                ,(?)
                ,(?)
                ,(?)
                ,(?)
                ,(?)
                ,(?)
                ,(?)
                ,(?)
                ,(?)
                ,(?))'''})

    insert_queries['base'].update({'abstractText': '''INSERT INTO [Pubmed_Abstracttext]
                   ([Medlinecitation_id]
                   ,[abstracttext]
                   ,[label]
                   ,[nlmcategory]
                   ,[CreatedDate])
             VALUES
                   ((?)
                   ,(?)
                   ,(?)
                   ,(?)
                   ,(?))'''})

    insert_queries['base'].update({'author': '''INSERT INTO [Pubmed_author]
                   ([Medlinecitation_id]
                   ,[authfore]
                   ,[authinit]
                   ,[authlast]
                   ,[author]
                   ,[validyn]
                   ,[CreatedDate])
             VALUES
                   ((?)
                   ,(?)
                   ,(?)
                   ,(?)
                   ,(?)
                   ,(?)
                   ,(?))'''})

    insert_queries['base'].update({'meshheading': '''INSERT INTO [Pubmed_meshheading]
                   ([Medlinecitation_id]
                   ,[descriptorname]
                   ,[majortopicyn]
                   ,[meshheading]
                   ,[type]
                   ,[ui]
                   ,[CreatedDate])
             VALUES
                   ((?)
                   ,(?)
                   ,(?)
                   ,(?)
                   ,(?)
                   ,(?)
                   ,(?))'''})

    insert_queries['master'].update({'medlinecitation': '''INSERT INTO Pubmed_Master_Medlinecitation
                    ([PMID]
                    ,[Title]
                    ,[JournalTitle]
                    ,[JournalCountry]
                    ,[LinktoPubmed]
                    ,[Pub_day]
                    ,[Pub_month]
                    ,[Pub_year]
                    ,[Pubdate]
                    ,[MedlineDate]
                    ,[CreatedDate]
                    ,[ModifiedDate])
                SELECT 
                     [PMID]
                    ,[Title]
                    ,[JournalTitle]
                    ,[JournalCountry]
                    ,[LinktoPubmed]
                    ,[Pub_day]
                    ,[Pub_month]
                    ,[Pub_year]
                    ,[Pubdate]
                    ,[MedlineDate]
                    ,[CreatedDate]
                    ,[CreatedDate]
                FROM
                    Pubmed_Medlinecitation
                WHERE
                    PMID = (?)'''})

    insert_queries['master'].update({'abstractText': '''INSERT INTO Pubmed_Master_Abstracttext
                    (Medlinecitation_id,
                    abstracttext,
                    label,
                    nlmcategory,
                    CreatedDate,
                    ModifiedDate)
                    SELECT 
                    Medlinecitation_id,
                    abstracttext,
                    label,
                    nlmcategory,
                    CreatedDate,
                    CreatedDate 
                    FROM Pubmed_Abstracttext
                WHERE
                    Medlinecitation_id = (?)'''})

    insert_queries['master'].update({'author': '''INSERT INTO Pubmed_Master_Author
                    (Medlinecitation_id,
                    authfore,
                    authinit,
                    authlast,
                    author,
                    validyn,
                    CreatedDate,
                    ModifiedDate)
                SELECT 
                    Medlinecitation_id,
                    authfore,
                    authinit,
                    authlast,
                    author,
                    validyn,
                    CreatedDate,
                    CreatedDate 
                    FROM Pubmed_author
                WHERE
                    Medlinecitation_id = (?)'''})

    insert_queries['master'].update({'meshheading': '''INSERT INTO Pubmed_Master_meshheading
                    (Medlinecitation_id,
                    descriptorname,
                    majortopicyn,
                    meshheading,
                    type,
                    ui,
                    CreatedDate,
                    ModifiedDate)
                SELECT 
                    Medlinecitation_id,
                    descriptorname,
                    majortopicyn,
                    meshheading,
                    type,
                    ui,
                    CreatedDate,
                    CreatedDate 
                    FROM Pubmed_meshheading
                WHERE
                    Medlinecitation_id = (?)'''})

    update_queries.update({
        'medlinecitation': '''UPDATE [Pubmed_Master_Medlinecitation]
           SET [ModifiedDate] = (?)
            WHERE ID = (?) AND PMID = (?)'''
    })

    update_queries.update({
        'abstract_text':'''UPDATE Pubmed_Master_Abstracttext
           SET 
              [abstracttext] = (?),
              [label] = (?),
              [nlmcategory] = (?),
              [ModifiedDate] = (?)
            WHERE id = (?)'''
    })

    update_queries.update({
        'author': '''UPDATE [Pubmed_Master_Author]
           SET 
              [authfore] = (?),
              [authinit] = (?),
              [authlast] = (?),
              [author] = (?),
              [validyn] = (?),
              [ModifiedDate] = (?)
            WHERE id = (?)'''
    })

    update_queries.update({
        'meshheading': '''UPDATE [Pubmed_Master_meshheading]
           SET[descriptorname] = (?),
              [majortopicyn] = (?),
              [meshheading] = (?),
              [type] = (?),
              [ui] = (?),
              [ModifiedDate] = (?)
            WHERE [Medlinecitation_id] = (?)'''
    })

    select_queries['forBase'].update(
        {'ID_for_insertion': '''SELECT ID FROM Pubmed_Medlinecitation where PMID = (?)'''}
    )

    select_queries['forBase'].update(
        {'PMID': '''SELECT PMID FROM Pubmed_Medlinecitation where PMID = (?)'''}
    )

    select_queries['forBase'].update(
        {'existing_pmid': '''SELECT PMID FROM Pubmed_Medlinecitation'''}
    )

    select_queries['forBase'].update(
        {'ID_to_truncate': '''select count(ID) from Pubmed_Medlinecitation'''}
    )

    select_queries['forBase'].update(
        {'existing_abstracts': '''SELECT 
            id,
            abstracttext,
            label,
            nlmcategory 
            FROM Pubmed_Abstracttext 
            where Medlinecitation_id = (?)'''}
    )

    select_queries['forBase'].update(
        {'existing_authors': '''SELECT
            id,
            authfore,
            authinit,
            authlast,
            author,
            validyn, 
            FROM Pubmed_Author 
            where Medlinecitation_id = (?)'''}
    )

    select_queries['forBase'].update(
        {'existing_meshheading': '''SELECT
                authfore,
                authinit,
                authlast,
                author,
                validyn, 
                FROM Pubmed_meshheading 
                where Medlinecitation_id = (?)'''}
    )

    select_queries['forMaster'].update(
        {'PMID_Check': '''SELECT ID FROM Pubmed_Master_Medlinecitation where PMID = (?)'''}
    )

    select_queries['forMaster'].update(
        {'abstract_Check': '''SELECT 
            id,
            abstracttext,
            label,
            nlmcategory 
            FROM Pubmed_Master_Abstracttext 
            where Medlinecitation_id = (?)'''}
    )

    select_queries['forMaster'].update(
        {'author_Check': '''SELECT
            id, 
            authfore,
            authinit,
            authlast,
            author,
            validyn, 
            FROM Pubmed_Master_Author 
            where Medlinecitation_id = (?)'''}
    )

    select_queries['forMaster'].update(
        {'meshheading_Check': '''SELECT
            id, 
            descriptorname,
            majortopicyn,
            meshheading,
            type,
            ui, 
            FROM Pubmed_Master_meshheading 
            where Medlinecitation_id = (?)'''}
    )

    truncate_queries.update({'medlinecitation':'''truncate table Pubmed_Medlinecitation'''})

    truncate_queries.update({'abstractText': '''truncate table Pubmed_Abstracttext'''})

    truncate_queries.update({'author': '''truncate table Pubmed_author'''})

    truncate_queries.update({'meshheading': '''truncate table Pubmed_meshheading'''})

    return_queries = {
        'seq_b':select_queries['forBase'],
        'inq_b':insert_queries['base'],
        'trq':truncate_queries,
        'inq_m':insert_queries['master'],
        'seq_m':select_queries['forMaster'],
        'upq':update_queries
    }

    return return_queries