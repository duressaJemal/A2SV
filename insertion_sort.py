#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    a = arr[n-1]
    b= arr[0]
    for i in range(n-1):
        if arr[n-2-i] > a:
            arr[n-1-i] = arr[n-2-i]

            for i in range(n):
                print(arr[i], end = " ")
            print()
       
               
  
        else:
            arr[n-1-i] = a
            for i in range(n):
                print(arr[i], end = " ")
            print()
            break
    if arr[0] > a:
        arr[0] = a
        for i in range(n):
            print(arr[i], end = " ")
        print()
                        

            
        
insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])        
        
    


