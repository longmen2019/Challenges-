# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 10:52:47 2021

@author: men_l
"""

numDays = int(input("How many day's temperature? "))
total = 0
for i in range (1, numDays+1):
    nextDay = int(input("Day" + str(i) + "'s high temp: "))
    total+= nextDay 
avg = round(total/numDays,2)
print("\nAverage = " + str(avg))
