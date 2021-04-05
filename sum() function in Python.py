# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 22:02:01 2021

@author: User
"""

#python code to demonstrate the working of sum
numbers = [1,2,3,4,5,1,4,5]
#start parameter is not provided
Sum = sum(numbers)
print(Sum)
#start = 10
Sum = sum(numbers,10)
print(Sum)

#python code to demonstrate the exception of sum
# arr = ["a"]
# #start parameter is not provided
# Sum = sum(arr)
# print(Sum)
# #start = 10
# Sum = sum(arr,10)
# print(Sum)

#python code to demonstrate he practical application of sum()
numbers = [1,2,3,4,5,1,4,5]
#start = 10
Sum = sum(numbers)
average = Sum/len(numbers)
print(average)
