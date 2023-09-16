import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    
    bill.pop(k)
    actual = sum(bill) // 2
    
    result = None
    
    if b - actual != 0:
        result = b - actual
    else:
        result = "Bon Appetit"
    
    return result

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    result = bonAppetit(bill, k, b)
    
    print(result)