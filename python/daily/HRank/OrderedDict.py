'''
You are the manager of a supermarket.
You have a list of  items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items, .
The next  lines contains the item's name and price, separated by a space.
'''

from collections import OrderedDict
import re

products = OrderedDict()

if __name__ == '__main__':
    num = int(input())
    
    for _ in range(num):
        text = input()
        price = int(re.sub(r'\D', "", text))
        product = text.split(str(price))[0].strip()
        
        if product not in products.keys():
            products[product] = price
        else:
            update_price = products[product] + price
            products[product] = update_price
    
    for k, v in products.items():
        print(k, v)