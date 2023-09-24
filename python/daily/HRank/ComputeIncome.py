'''
A shop owner has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay Y amount of money only if they get the shoe of their desired size.

Task is to compute how much money is earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

Sample input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

'''

from collections import Counter as c

income = list()

if __name__ == '__main__':
    # Store total shoes (although the code does not use it)
    num_shoes = int(input())
    # Store shoe sizes as a list
    _sizes = list(map(int, input().split()))
    # Convert list of 'shoe sizes: count' to dictionary using Counter function
    shoe_sizes_inv = c(_sizes)
    # Store number of customers
    num_custs = int(input())
    
    # Loop through customers demand
    for _ in range(num_custs):
        size, cost = map(int, input().split())
        
        if size in shoe_sizes_inv.keys() and shoe_sizes_inv[size] > 0:
            shoe_sizes_inv[size] -= 1
            income.append(cost)
    
    total_income = sum(income)
    print(total_income)