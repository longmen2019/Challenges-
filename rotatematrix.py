# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 08:19:10 2021

@author: men_l
"""

import numpy as np
myArray = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
print(myArray)

def rotatematrix(matrix):
    n = len(matrix)
    for layer in range (n//2):
        first = layer
        last = n - layer -1 
        for i in range (first , last):
            top = matrix [layer] [i]
            matrix[layer][i] = matrix[-i-1][layer]
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
    return matrix
print(rotatematrix(myArray))