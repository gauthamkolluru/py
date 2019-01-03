import os

#print(os.listdir('/home/gautham'))

file_name = '/home/gautham/zingarelli2005.txt'

words = [word.strip().lower() for word in open(file_name)]

words = [word[0] for word in words]

print(words)