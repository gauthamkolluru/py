#!/bin/python3

import os
import sys
import copy

#
# Complete the hyperStrings function below.
#
def hyperStrings(m, H):
    # Write your code here.
    str_list=copy.deepcopy(H)
    for strin in str_list:
        if len(strin)<m:
            for i in range(1,m+1):
                if len(strin*i)<=m and (strin*i) not in str_list:
                    str_list.append(strin*i)
                    print(str_list)
            # for i in range(1,m+1):
            #     for j in range(len(H)):

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

    # fptr.write(str(result) + '\n')

    # fptr.close()
