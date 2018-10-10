import os

search_directory = r'D:\PharmSource\advantageCFClient'

count = 0
for path, directories, files in os.walk(search_directory):
    for file in files:
        file_name = os.path.join(path, file)
        try:
            with open(file_name, 'r') as fn:
                count += 1
                if 'Sorry' in fn.read():
                    print(file_name)
        except Exception as e:
            print('error in file: ', file_name)

print(count)
