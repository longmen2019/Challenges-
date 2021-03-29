# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 22:38:46 2021

@author: User
"""
"""
Given a list of numbers return whether any two sums to k.
for example, given [10,15,3,7] and k of 17, return True since 10+ 7 = 17
"""

def check_sum(array, k):
    num = set()
    for i in array:
        if i in num:
            return True
        num.add(k-i)    
    else:
        return False
    
print(check_sum([10,15,3,7] , 17))

