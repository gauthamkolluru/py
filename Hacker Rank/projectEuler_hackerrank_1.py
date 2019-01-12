#!/bin/python3

import sys


t = int(input().strip())
m_l = []
for a0 in range(t):
    n = int(input().strip())
    m_l.append(n)

for m in m_l:
    f_l = []
    for i in range(m):
        if i%3 == 0:
            f_l.append(i)
        elif i%5 == 0:
            f_l.append(i)
    print(sum(f_l))