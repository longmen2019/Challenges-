# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:50:35 2021

@author: men_l
"""
import numpy as np

myList=[1,20,30,20,40,50,60,70,80] 

def searchduplicate(list):
    emptylist=[]
    for i in range (len(list)):
        for j in range (i+1, len(list)):
            if list[i] == list[j]:
                emptylist.append(list[i])
                print(emptylist)
                
searchduplicate(myList)

def isunique(list):
    empty = []
    for i in list:
        if i in empty:
            print(i)
            False
        else:
            empty.append(i)
    return True
print(isunique(myList))
                