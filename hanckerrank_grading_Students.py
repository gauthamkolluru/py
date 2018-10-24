#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    for grade in grades:
        if grade >= 38:
            round_tip = (grade//5)+1
            if (round_tip*5)-grade < 3:
                i = grades.index(grade)
                grades.pop(i)
                grades.insert(i,round_tip*5)
    return grades
        

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)

    # f.write('\n'.join(map(str, result)))
    # f.write('\n')

    # f.close()
