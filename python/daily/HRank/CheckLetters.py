'''
Inn this challenge, you will be given  integers, n and m.
There are n words, which might repeat, in word group A. There are m words belonging to word group B.
For each m words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Example

Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions 1 and 3 in group A. The second word, 'c', does not appear in group A, so print -1.

Expected output:

1 3
-1

'''

from collections import defaultdict

default = defaultdict(list)

if __name__ == '__main__':
    n, m = map(int, input().split())
    
    for _ in range(n):
        letter = input()
        default[letter].append(_ + 1)
        
    for i in range(m):
        check = input()
        if check in default:
            print(' '.join([str(i) for i in default[check]]))
        else:
            print(-1)