# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 18:18:37 2021

@author: men_l
"""
myarray = list(range(21))
print(myarray)

import numpy as np
myarray = np.array(myarray)
print(myarray)

def findIndexNumber(array, value):
    for i in range (len(array)):
        if array[i] == value:
            print(i)
            
findIndexNumber(myarray, 13)