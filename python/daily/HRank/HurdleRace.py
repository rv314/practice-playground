'''
A video player plays a game in which the character competes in a hurdle race. Hurdles are of varying heights, 
and the characters have a maximum height they can jump. There is a magic potion they can take that will increase
their maximum jump height by unit for each dose. How many doses of the potion must the character take to be able 
to jump all of the hurdles. If the character can already clear all of the hurdles, return 0.

Example
height = [1, 2, 3, 3, 2]
k = 1
The character can jump 1 unit high (k) initially and must take doses of potion to be able to jump all of the hurdles.

Sample Input 0

5 4
1 6 3 5 2

Sample Output 0

2

'''
import os

def hurdleRace(k, height):
    
    result = 0
    
    for h in height:
        if k > h:
            result
        else:
            result = max(height) - k
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
