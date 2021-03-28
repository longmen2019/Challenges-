# -*- coding: utf-8 -*-
"""


Created on Sat Mar 27 22:14:40 2021

@author: User
"""


# Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:
# 22=4, 23=8, 24=16, 25=32
# 32=9, 33=27, 34=81, 35=243
# 42=16, 43=64, 44=256, 45=1024
# 52=25, 53=125, 54=625, 55=3125
# If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

# The math.pow() method returns the value of x raised to power y.
import math
# Create set() for a custom iterable object
sequence = set()
for a in range (2,6):
    for i in range (2,6):
# The add() method adds an element to the set.
# If the element already exists, the add() method does not add the element.
        sequence.add(int(math.pow(a,i)))
print(sorted(sequence))

