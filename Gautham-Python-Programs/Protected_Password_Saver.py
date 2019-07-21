# An application to safely save asll your passowrds in an encrypted 'Key:Value' format in a file in your computer 
# and getting the file hidden
# You can always retrieve/change password using the 'Key'(s) as and when required

# Let's write the following functions for doing the tasks as above:
#TODO:
#  1. function for creating / Accessing the file #Done
#  2. function to save (add / modify) a username and password
#  3. function to retrieve a password by providing the username as a key
#  4. function to turn the file to hidden mode

import os, random
import datetime
import shutil



def get_file_name():
    filename = 'gPassowrd_Managerk.json'
    root = 'c:\\users'
    file_not_found = 0

    if os.path.exists(root):
        hostName = os.environ['COMPUTERNAME']
        if os.path.exists(root+'\\'+hostName):
            path1 = os.path.join(root,hostName)
            print(path1)
        if os.path.exists(path1+'\\'+'Documents'):
            path2 = os.path.join(path1,'Documents')
            print(path2)

    if path2:
        file_not_found = 1
        for i,j,k in os.walk(path2):
            for file in k:
                if file == filename:
                    file_not_found = 0
                    return os.path.join(i,filename)

    # if root or file_not_found:
    #     # print('hi')
    #     for i,j,k in os.walk(root):
    #         for file in k:
    #             # print('hi')
    #             if file == filename:
    #                 print(i+filename)
    #                 file_not_found = 0
    #                 return i+filename

    if file_not_found:
        list_folders = []
        for folder in os.listdir(path2):
            # print('hi')
            if os.path.isdir(folder):
                # print('hi')
                list_folders.append(folder)
        rand_num = random.randint(0,len(list_folders)-1)
        if os.path.isdir(path2+'\\'+list_folders[rand_num]):
            path_to_file = path2+'\\'+list_folders[rand_num]
            # dateval = datetime.datetime.now()
            with open(os.path.join(path_to_file,filename),'a') as pff:
                pff.write('\\n')
            file_not_found = 0
        return os.path.join(path_to_file,filename)
    


def main():
    file_path_name = get_file_name()
    print(file_path_name)



if __name__ == '__main__':
    main()
