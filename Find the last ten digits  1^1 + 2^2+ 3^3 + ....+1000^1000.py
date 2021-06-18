# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 22:22:43 2021

@author: User
"""
# Find the last ten digits of the series, Find the last ten digits  1^1 + 2^2+ 3^3 + ....+1000^1000

L = 1000
d = 10 ** 10
#s = sum(pow(n,n,d) for n in range (1, L + 1))
s = sum(pow(n,n)for n in range (1, L+1))


print("Project Euler 48 Solution = %d" % (s%d))

#Project Euler 48 Solution= 9110846700
