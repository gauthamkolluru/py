if medline.find('PMID'):
        pmid = medline.find('PMID').text
    else:
        pmid = ''
    # if medline.find('DateRevised').find('Year'):
    dateval_year = medline.find('DateRevised').find('Year').text
    # else:
    #     dateval_year = ''
    # if medline.find('DateRevised').find('Month'):
    dateval_month = medline.find('DateRevised').find('Month').text
    # else:
    #     dateval_month = ''
    # if medline.find('DateRevised').find('Day'):
    dateval_day = medline.find('DateRevised').find('Day').text
    # else:
    #     dateval_day = ''
    # if datetime(int(dateval_year),int(dateval_month),int(dateval_day)):
    dateval = datetime(int(dateval_year),int(dateval_month),int(dateval_day))
    dateval = dateval.strftime('%d/%m/%Y')
    # else:
    #     dateval = ''
    if medline.find('Article').find('Journal').find('Title'):
        title = medline.find('Article').find('Journal').find('Title').text
    else:
        title = ''
    if medline.find('Article').find('ArticleTitle'):
        articleTitle = medline.find('Article').find('ArticleTitle').text
    else:
        articleTitle = ''
    if medline.find('Article').find('Abstract'):
        if medline.find('Article').find('Abstract').find('AbstractText'):
            abstractText = medline.find('Article').find('Abstract').find('AbstractText').text
        else:
            abstractText = ''
    else:
        abstractText = ''
    # if medline.find('Article').find('AuthorList').findall('Author'):
    if medline.find('Article').find('AuthorList'):
        if medline.find('Article').find('AuthorList').findall('Author'):
            for authors in medline.find('Article').find('AuthorList').findall('Author'):
                if authors.find('LastName'):
                    LastName = authors.find('LastName').text
                else:
                    LastName = ''
                if authors.find('ForeName'):
                    ForeName = authors.find('ForeName').text
                else:
                    ForeName = ''
                if authors.find('Initials'):
                    initials = authors.find('Initials').text
                else:
                    initials = ''
                authorList.append({'LastName':LastName,'ForeName':ForeName, 'Initials':initials})
        else:
            LastName = ''
            ForeName = ''
            initials = ''
            authorList.append({'LastName':LastName,'ForeName':ForeName, 'Initials':initials})
    else:
        LastName = ''
        ForeName = ''
        initials = ''
        authorList.append({'LastName':LastName,'ForeName':ForeName, 'Initials':initials})
    if medline.find('MedlineJournalInfo').find('Country'):
        country = medline.find('MedlineJournalInfo').find('Country').text
    else:
        country = ''
    if medline.find('MeshHeadingList'):
        if medline.find('MeshHeadingList').findall('MeshHeading'):
            for mHeading in medline.find('MeshHeadingList').findall('MeshHeading'):
                descName = mHeading.find('DescriptorName').get('UI')
                desc = mHeading.find('DescriptorName').text
                mHeading_desc.append({'descName':descName, 'desc':desc})    
        else:
            descName = ''
            desc = ''
            mHeading_desc.append({'descName':descName, 'desc':desc})
    link_to_pubmed = f'https://www.ncbi.nlm.nih.gov/pubmed/{pmid}'
    current_date = datetime.now()
    # query = '''INSERT INTO Pubmed_Medlinecitation_Gautham
    #     ([PMID]
    #     ,[Title]
    #     ,[JournalTitle]
    #     ,[JournalCountry]
    #     ,[LinktoPubmed]
    #     ,[Pub_day]
    #     ,[Pub_month]
    #     ,[Pub_year]
    #     ,[Pubdate]
    #     ,[CreatedDate])
    # VALUES
    #     (%s
    #     ,%s
    #     ,%s
    #     ,%s
    #     ,%s
    #     ,%s
    #     ,%s
    #     ,%s
    #     ,%s
    #     ,%s)'''
    # cursor.execute(query,(pmid,title,articleTitle,country,link_to_pubmed,dateval_day,dateval_month,dateval_year,dateval,current_date))