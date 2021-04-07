# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 22:18:08 2021

@author: User
"""

#import divisors() method from sympy
from sympy import divisors

n = 84
#Use divisors () method
divisors_n = divisors(n)

print("The divisors of {} : {}".format(n, divisors_n))


#import divisors() method from sympy
from sympy import divisors
n = -210

#Use divisors () method
divisors_n = list(divisors(n, generator= True))

print("The divisors of {}: {}".format(n , divisors_n))
