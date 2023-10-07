'''
There is a large pile of socks that must be paired by color. Given an array of integers representing
 the color of each sock, determine how many pairs of socks with matching colors there are.

STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

Sample Output

3

'''

#!/bin/python3

import os

from collections import Counter


def sockMerchant(n, ar):
    # O(n)
    pairs = 0
    sock_count = {} # can also use Counter
    
    for item in ar:
        if item not in sock_count:
            sock_count[item] = 1
        else:
            sock_count[item] += 1
    
    for k, v in sock_count.items():
        if v > 1:
            pairs += v // 2

    return pairs
                
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()