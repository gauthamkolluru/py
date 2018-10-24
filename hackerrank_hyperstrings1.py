#!/bin/python3

import os
import sys
import copy
import itertools

#
# Complete the hyperStrings function below.
#
def hyperStrings(m, H):
    # Write your code here.
    str_list = H
    # temp_str = ''
    for item in str_list:
        for i in range(m+1):
            if (item*i) not in str_list:
                str_list.append(item*i)
    for item1 in str_list:
        temp_str = item1
        for item2 in str_list:
            for i in range(m+1):
                if len(temp_str+(item2*i)) <= m and (temp_str+(item2*i)) not in str_list:
                    str_list.append((temp_str+(item2*i)))
                if len((temp_str*i)+item2) <= m and ((temp_str*i)+item2) not in str_list:
                    str_list.append(((temp_str*i)+item2))
                if len(item2+(temp_str*i)) <= m and (item2+(temp_str*i)) not in str_list:
                    str_list.append(item2+(temp_str*i))
                if len((item2*i)+temp_str) <= m and ((item2*i)+temp_str) not in str_list:
                    str_list.append((item2*i)+temp_str)
    temp_str = ''
    for item1 in str_list:
        temp_str += item1
        for i in range(m+1):
                if len(temp_str+(item2*i)) <= m and (temp_str+(item2*i)) not in str_list:
                    str_list.append((temp_str+(item2*i)))
                if len((temp_str*i)+item2) <= m and ((temp_str*i)+item2) not in str_list:
                    str_list.append(((temp_str*i)+item2))
                if len(item2+(temp_str*i)) <= m and (item2+(temp_str*i)) not in str_list:
                    str_list.append(item2+(temp_str*i))
                if len((item2*i)+temp_str) <= m and ((item2*i)+temp_str) not in str_list:
                    str_list.append((item2*i)+temp_str)

    

    return str_list

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    H = []

    for _ in range(n):
        H_item = input()
        H.append(H_item)

    result = hyperStrings(m, H)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
