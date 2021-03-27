# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:43:57 2021

@author: User
"""
# Write a function that stutters a word as if someone is struggling to read it.
#  The first two letters are repeated twice with an ellipsis ... and 
#  space after each, and then the word is pronounced with a question mark ?.

def stutter (str):
    #str[:2] will return the first two character of the word
    return str[:2] + '... ' + str[:2] + '... ' + str + '?'