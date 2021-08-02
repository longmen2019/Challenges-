# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:20:25 2021

@author: men_l
"""
import numpy as np
myarray = np.array(list(range(10)))
def find_maxproduct (array):
    maxproduct = 0
    for i in range (len(array)):
        for j in range (i+1, len(array)):
            if array[i] * array[j] > maxproduct:
                maxproduct = array[i] * array[j]
                pairs = str(array[i]) + "," + str(array[j])
    print(pairs)
    print(maxproduct)
find_maxproduct(myarray)