def main():
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

    file_wo_gz = ftp_gz_grab_extract.ftp_gz_grab_extract()

    if file_wo_gz:
        retval = xml_BaseTables.xml_BaseTables(file_wo_gz)

    if retval == 0:
        baseTables_MasterTables.baseTables_MasterTables()



if __name__ == '__main__':
    main()
