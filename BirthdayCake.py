#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    if not(m > 12) and not(d > 31):
        if m == 1:
            return s.count(d) if d in s else 0
        elif m == len(s):
            return 1 if d == sum(s) else 0
        else:
            return [sum(s[i:i+m])for i in range(len(s))].count(d)
    return 0
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
