import os
import shutil
import time

time.sleep(45)

source_folder = '/home/gautham/Downloads/'

destination_folders = {
    ('doc', 'docx'):'/home/gautham/Documents/DOCS/',
    ('pdf'):'/home/gautham/Documents/PDFs/',
    ('txt', 'md'):'/home/gautham/Documents/TXTs/',
    ('ppt', 'pptx', 'odt'):'/home/gautham/Documents/Presentations/',
    ('xls', 'xlsx', 'csv', 'ods'):'/home/gautham/Documents/XLSs/',
    ('mp3'):'/home/gautham/Music/',
    ('mp4', 'mkv', 'mpeg', 'avi'):'/home/gautham/Videos/',
    ('jpg', 'jpeg', 'png'):'/home/gautham/Pictures/',
    ('zip', 'tar', 'gz', 'tgz', 'rar'):'/home/gautham/Documents/ZIPs/',
    ('deb', 'pkg'):'/home/gautham/Documents/Software-Packages/'
    }

# We os.walk() method to parse through the downloads folder and get the details of all the files

# abp (Absolute Paths) = absolute path of the source folder

# ff (files / folders) = list of files / folders in the current path

# rlp (Relative Paths) = list of relative paths of each of the files in the current and it's sub folders

# => combining abp & rlp will will the absolute path of each file in the source folder and it's sub-folders

for abp,ff,rlp in os.walk(source_folder):
    for each_file in rlp:
        folder_key = ''
        for extention in destination_folders.keys():
            if not folder_key:
                folder_key = extention if each_file.split('.')[-1].lower() in extention else ''
        if folder_key:
            shutil.move(os.path.join(abp, each_file), os.path.join(destination_folders[folder_key], each_file))
        #     print(each_file + ' has been moved to ' + destination_folders[folder_key])
        # else:
        #     print("folder key did not exist" + each_file)

# Now let's place this in the scheduler and make it run everytime the system is turned on.

# Before that, this file is currently in the folder where I keep my incomplete automation works and for now, 

# it is completed, I shall move to my permanent folder for such automation files.
