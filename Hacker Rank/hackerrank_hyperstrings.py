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
    str_list = ['']
    if len(H)>1:
        str_list.extend(H)
    for s1 in str_list:
        for s2 in str_list:
            if len(s2+s1) <= m:
                if s2+s1 not in str_list:
                    str_list.append((s2+s1))
                if s1+s2 not in str_list:
                    str_list.append((s1+s2))
            else:
                break
            # print(str_list)

    return len(str_list)

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
