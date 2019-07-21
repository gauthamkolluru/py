#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs  = 0
    while ar:
        i = ar[0]
        if ar.count(i)>1:
            pairs += ar.count(i)//2
        while i in ar:
            ar.remove(i)
    return pairs


n = 15
ar = [6,5,2,3,5,2,2,1,1,5,1,3,3,3,5]

result = sockMerchant(n,ar)

print(result)
