# Lets automate the process of deleting any empty folders from the system

import os
import shutil

# Folders to look into - fl

fl = [
    '/home/gautham/Documents',
    '/home/gautham/Downloads',
]

def remove_empty_folders(folder_path):
    if os.path.isdir(folder_path):
        if os.listdir(folder_path):
            for abp, folder_list, rlp in os.walk(folder_path):
                for each_dir in folder_list:
                    remove_empty_folders(os.path.join(abp, each_dir))
        else:
            return os.rmdir(folder_path)

for f in fl :
    remove_empty_folders(f)