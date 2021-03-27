# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:00:55 2021

@author: User
"""

divide = []
for x in range (1000):   
    if x % 3 == 0 or x % 5 ==0:        
        divide.append(x)
print(sum(divide))