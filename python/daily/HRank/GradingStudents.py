#!/bin/python3
'''
Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.

Sam is a professor at the university and likes to round each student's grade according to these rules:
    1. If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
    2. If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

Examples:

grade = 84 round to 85 (85 - 84 is less than 3)
grade = 29 do not round (result is less than 40)
grade = 57 do not round (60 - 57 is 3 or higher)

Given the initial value of grade for each of Sam's N students, write code to automate the rounding process. 

'''
import os

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    result = [grade + 5 - (grade % 5) if grade >= 38 and 5 - (grade % 5) < 3 else grade for grade in grades]
        
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()