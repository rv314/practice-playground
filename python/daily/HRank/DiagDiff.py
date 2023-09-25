'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
'''

import os

def diagonalDifference(arr):
    # Write your code here
    left = 0
    right = 0
    for i, val in enumerate(arr):
        left += arr[i][i]
        right += arr[i][len(arr)-1-i]
    return abs(left - right)
        
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()