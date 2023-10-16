#!/bin/python3
'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with  places after the decimal.
'''
import math
import os
import random
import re
import sys

def divide(element, length):
    return element / length

def plusMinus(arr):
    
    pos = 0
    neg = 0
    zero = 0
    store = list()
    
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    
    store.append(pos)
    store.append(neg)
    store.append(zero)
    
    store = [divide(i, len(arr)) for i in store]
    
    return store
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    results = plusMinus(arr)
    
    for result in results:
        print("% .6f" %result)