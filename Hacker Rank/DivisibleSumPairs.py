#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the divisibleSumPairs function below.
def possibleCombinations(arr):
    return [sum(i) for i in itertools.combinations(arr,2)]
def divisibleSumPairs(n, k, ar):
    if not (n <= 1):
        if k == 0:
            return 0
        if k == 1:
            return len(possibleCombinations(ar))
        if k > 1:
            return len([i for i in possibleCombinations(ar) if i%k == 0])

    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
