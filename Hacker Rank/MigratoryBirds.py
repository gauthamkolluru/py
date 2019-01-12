#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def maxFreq(ar):
    return max([ar.count(i) for i in set(ar)])
def migratoryBirds(arr):
    if len(arr):
        if len(arr) == 1:
            return arr[0]
        else:
            maxVal = maxFreq(arr)
            if maxVal == 1:
                return arr
            else:
                return min([i for i in set(arr) if arr.count(i) == maxVal])
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
