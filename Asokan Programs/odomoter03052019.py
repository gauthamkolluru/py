num_list = [i for i in range(12,90) if str(i)[0] < str(i)[1]]
n = int(input())
if n in num_list:
    num_ind = -1 if n == num_list[-1] else num_list.index(n)
    print('previous reading: ', num_list[num_ind - 1])
    print('next reading: ', num_list[num_ind + 1])
else:
    print('Invalid Input')