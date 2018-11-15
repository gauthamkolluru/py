import ftp_gz_grab_extract
import xml_BaseTables
import baseTables_MasterTables

def main():
    file_wo_gz = ftp_gz_grab_extract.ftp_gz_grab_extract()

    # print(file_wo_gz)

    for file in file_wo_gz:
        if file:
            retval = xml_BaseTables.xml_BaseTables(file)
            print(f'Completed XML Parsing for {file}')

        if retval == 0:
            retval_2 = baseTables_MasterTables.baseTables_MasterTables()
            print(f'Completed transfering Base table data to Master tables for {file}')

        if retval_2 == 0:
            print('Exec Completed!')



if __name__ == '__main__':
    main()
