#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    cost = 0
    for i in range(3):
        if s[i][0]+s[i][1]+s[i][2] != 15:
            var = abs(s[i][0]+s[i][1]+s[i][2] - 15)
            

    
    
    return s


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
