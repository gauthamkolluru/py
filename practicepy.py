#values = range(10)

#for i in values:
#    print(i)


#i = 0
#while(i<10):
#    print(i)
#   i = i+1

# write a loop for brushing teeth:

# teeth_exists = 'yes'
# while(teeth_exists == 'yes'):
#     print('brush daily')
#     teeth_exists = 'no'

my_file = 'transcripts123'

my_folder = ['file1','file2','file3','file143','file123','file8752363','gautham','sravya','transcripts','varma','swathi','coding','sastra','vizag','shanthipuram','akkayyapalem','goodhachari','something else','maybe','finally']

file_not_found_var = 0
for file_from_my_folder in my_folder:
    if(file_from_my_folder == my_file):
        print(my_file)
        break
    else:
        file_not_found_var = file_not_found_var+1
        # print('file not found')
if file_not_found_var == len(my_folder):
    print('file not found')