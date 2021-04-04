# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:03:37 2021

@author: User
"""

# The series, 1^1 + 2^2 + 3^3 + … + 10^10 = 10405071317.
import math
potential_solution = set()
for i in range (1,11):
    potential_solution.add(int(math.pow(i,i)))
    
print(sum(potential_solution))

    