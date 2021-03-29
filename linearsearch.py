# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:01:47 2021

@author: User
"""
"""
Given an array of a distinct integer sorted in ascending order. 
Write a function that return a fixed point in the array, else return -1
"""
def fixed_point(array, n):    
    for i in range (n):
        
        if array[i] == i :
            return i
    else:
        return -1
array = [-10,-5,0,3,7]
n = len(array)     
print(fixed_point(array,n))