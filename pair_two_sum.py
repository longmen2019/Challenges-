# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 17:34:58 2021

@author: men_l
"""

def findpair(num, target):
    for i in range (len(num)):
        for j in range (i+1, len(num)):
            if num [i] == num[j]:
                continue
            elif num [i] + num[j] == target:
                print(i,j)
        
print(findpair([1,2,3,2,3,4,5,6] , 6))
                