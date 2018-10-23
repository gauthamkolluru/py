#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # Write your code here.
    s1 = []
    if 'am' in s.lower():
        s1 = s.lower().split('am')
        s1[0] = s1[0].split(':')
        if int(s1[0][0])>=1 and int(s1[0][0])<=12 and int(s1[0][1])>=00 and int(s1[0][1])<=59 and int(s1[0][2])>=00 and int(s1[0][2])<=59:
            if s1[0][0]=='12':
                s1[0][0]='00' 
            return ':'.join(s1[0])
    elif 'pm' in s.lower():
        s1 = s.lower().split('pm')
        s1[0] = s1[0].split(':')
        if int(s1[0][0])>=1 and int(s1[0][0])<=12 and int(s1[0][1])>=00 and int(s1[0][1])<=59 and int(s1[0][2])>=00 and int(s1[0][2])<=59:
            if s1[0][0] == '12':
                return ':'.join(s1[0])
            else:
                s1[0][0] = str(int(s1[0][0])+12)
            return ':'.join(s1[0])
    return None

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)

    # f.write(result + '\n')

    # f.close()
