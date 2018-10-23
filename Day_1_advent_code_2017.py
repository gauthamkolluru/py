number = input('Enter the Number: ')
sum = 0
numlen = len(number)
for i in range(int(numlen/2)):
    print(i,number[i],number[int(numlen/2)+i])
    if number[i] == number[int(numlen/2)+i]:
        sum = sum + int(number[i])*2
    


print(sum)