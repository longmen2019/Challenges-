# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 21:22:28 2021

@author: men_l"""

"""A palindromic number reads the same both ways. The largest plindrome made from the product of two 2-digit numbers is 
9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers"""

def is_palindrome(i):
    #convert integer i into string and compare the char
    # look at that text string and read it backward
    return str(i) == "".join(reversed(str(i)))

max_p = 0

for i in range(100, 1000): #three digit numbers
    for j in range(i, 1000): #looping through the number and adding 1 each time
        p = i * j
        if is_palindrome(p) and p > max_p:
            max_p = p

print(max_p)