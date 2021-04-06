# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 22:40:59 2021

@author: User
"""

#finding the maximum of 3 integer variables

var1 = 4
var2 = 8
var3 = 2

max_val = max(var1, var2, var3)
print(max_val)

#finding the maximum of three string variables. By default, it will return the string with the maximum lexographic value
var1 = "geeks"
var2 = "for"
var3 = "geek"

max_val = max(var1, var2, var3)
print(max_val)

var1 = "geeks"
var2 = "for"
var3 = "geek"

max_val = max(var1, var2, var3)
print(max_val)

# #Example 4 if we pass parameters of different datatypes, then an exception will be raised
# integer = 5
# string = "geek"
# max_val = max(integer, string)
# print(max_val)

#Example 1 finding the lexographically maximum character in a string.
string = "GeeksforGeek"
max_val = max(string)
print(max_val)


#Example 2 finding the lexographically maximum string a string list.
string_list = ["Geeks" , "for" , "Geeks"]
max_val = max(string_list)
print(max_val)

#Example 3 Fiding the longest string in a string list
string_list = ["Geeks" , "for" , "Geek"]
max_val = max(string_list , key = len)
print(max_val)

#Example 4  if the iterable is empty, the default value will be displayed.
dictionary  = {}
max_val = max(dictionary, default = {1: "Geek"})
print(max_val)