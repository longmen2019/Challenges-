# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:05:52 2021

@author: User
"""

# Python program showing use of format() method 

# Using format() method

print('I love {} for  "{}"'.format('Geeks' , 'Geeks'))

# Using format() method and refering
# A position of the object

print('{0} and {1}'.format('Geeks' , 'Portal'))

print('{1} and {0}'.format('Geeks', 'Portal'))

#The above formatting can also be done by using f-Strings
#Although, this features work only with python 3.6 or above.

print(f"I love {'Geeks'} for \"{'Geeks'}!\"")

# using format () method and refering
# a position of the object

print(f"{'Geeks'} and {'Portal'}")
      
      
    