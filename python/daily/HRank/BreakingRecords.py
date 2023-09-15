#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    low_score = scores[0]
    high_score = scores[0]
    low_scores = list()
    high_scores = list()
    
    for i in range(1, len(scores)):
        if scores[i] < low_score:
            low_score = scores[i]
            low_scores.append(low_score)
        elif scores[i] > high_score:
            high_score = scores[i]
            high_scores.append(high_score)
            
    return [len(high_scores), len(low_scores)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()