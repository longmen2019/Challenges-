# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 22:35:41 2021

@author: User
"""

#Python program to show format() is used in dictionary

tab = {'geeks': 4127, 'for':4098 , 'geek':8637678}

#Using format() in dictionary
print('Geeks: {0[geeks]:d}; For:{0[for]:d};'
      'Geeks: {0[geek]:d}'.format(tab))

data =dict(fun="GeeksForGeeks" , adj = "Portal")

#Using format() in dictionary
print("I love {fun} computer {adj}".format(**data))
