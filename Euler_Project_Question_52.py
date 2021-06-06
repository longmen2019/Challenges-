# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
""" It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

 Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."""

#  Write up a function
def check (a,b):  
  alist = list(str(a))
  alist.sort()
  blist = list(str(b))
  blist.sort()
  if alist == blist: 
    return True
  else:
    return False
start = 100000
end = int (start*1.6666666 + 1)

for n in range (start, end):
  res = []
  for j in range (2,7):
    mult = j*n
    if check(n,mult) == False :
        break
    res.append(mult)
  if check(n , mult) == False: 
      continue
  print (n, res)
