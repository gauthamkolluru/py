#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_pos = 0
    count_neg = 0
    count_z = 0
    for i in arr:
        if i>0:
            count_pos += 1
        elif i<0:
            count_neg += 1
        else:
            count_z += 1
    print("%.6f" % (count_pos/len(arr)))
    print("%.6f" % (count_neg/len(arr)))
    print("%.6f" % (count_z/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
