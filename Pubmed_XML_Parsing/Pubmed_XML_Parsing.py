import ftp_gz_grab_extract
import xml_BaseTables
import baseTables_MasterTables

def main():
    file_wo_gz = ftp_gz_grab_extract.ftp_gz_grab_extract()

    file_parsed = []
    # print(file_wo_gz)

    for file in file_wo_gz:
        if file and file.split('.')[-1].lower() == 'xml' and file not in file_parsed:
            retval = xml_BaseTables.xml_BaseTables(file)
        else:
            continue

        # retval = 0
        if retval == 0:
            file_parsed.append(file)
            print(f'Completed XML Parsing for {file}')
            retval_2 = baseTables_MasterTables.baseTables_MasterTables()
            print(f'Completed transfering Base table data to Master tables for {file}')

        if retval_2 == 0:
            print('Exec Completed!')
            with open(r'C:\Users\skolluru\Desktop\filenames.txt','a') as fn:
                fn.writelines(file_parsed[-1]+'\n')



if __name__ == '__main__':
    main()
