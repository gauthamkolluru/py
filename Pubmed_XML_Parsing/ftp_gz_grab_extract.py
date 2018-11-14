def ftp_gz_grab_extract():
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

    # Finding & Downloading the required file from the FTP server
    # file_name_dates = [{'fileName':file[0],'modifiedDate':file[1]['modify'][:7]} for file in files]


    prev_date = input('Enter date in YYYY/MM/DD format (if you want the latest just press enter)')
    if prev_date and (len(prev_date) == 8 or len(prev_date) == 10):
        prev_date = prev_date.replace('/', '')
        ftp = ftplib.FTP('ftp.ncbi.nlm.nih.gov')
        ftp.login()
        ftp.cwd('pubmed/updatefiles/')
        files = ftp.mlsd()
        file_name_dates = [{'fileName': file[0], 'modifiedDate': file[1]['modify'][:7]} for file in files]
        file_to_download = []
        for file in file_name_dates:
            if file['modifiedDate'] == prev_date:
                file_to_download.append(file[0])
        for file in file_to_download:
            if file.split('.')[-1].lower() == 'gz':
                req_file_name = file
                break
    else:
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
        urllib.request.urlretrieve(f'ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/{req_file_name}',
                                   f'd:\\{filename}')

    if os.path.exists(f'd:\\{file_wo_gz}'):
        pass
    else:
        with gzip.open(f'd:\\{filename}', 'rb') as go:
            with open(f'd:\\{file_wo_gz}', 'wb') as of:
                shutil.copyfileobj(go, of)

    return file_wo_gz
