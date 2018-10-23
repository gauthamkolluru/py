#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr,n):
    sum_dig1 = 0
    sum_dig2 = 0
    for i in range(n):
        sum_dig1 += arr[i][i]
    for i in range(n):
        sum_dig2 += arr[i][n-1-i]
    return abs(sum_dig1-sum_dig2)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
