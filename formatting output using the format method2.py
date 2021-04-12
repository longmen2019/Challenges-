# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 22:09:45 2021

@author: User
"""

#Python program showing
#A use of format() method

#Combining positional and keyword arguments
print('Number one portal is {0} , {1}, and {other}.'
      .format('Geeks' , 'for' ,  other='Geek'))

#Using format() method with number
print("Geeks: {0:2d} , Portal: {1:8.2f}".
      format(12, 00.546))

#Changing Positional Argument
print("Second argument: {1:3d} , first one: {0:7.2f}".
      format(47.42, 11))

print("Geeks: {a:5d} , Portal: {p:8.2f}".
      format(a=453 , p = 59.058))