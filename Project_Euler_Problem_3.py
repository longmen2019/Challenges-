# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 22:24:08 2021
https://www.youtube.com/watch?v=5kv9q7qgvlI

https://www.youtube.com/watch?v=Y3n-PA3QoAE
@author: men_l
"""
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

n = int(input("Enter a number: ")) # create a variable n of number that are seeking its prime factor 
i = 2 

while i * i < n: # using while loop i times itself and is less than the target number
    while n % i == 0: # also while n mod i and remainder is equal to 0
        n = n / i 
    i += 1 # i = i + 1
print (n)

#Prime number of 24
# 24 = 2 * 2 * 2 *3 because we cannot break down 2 and 3 anymore 

# """"PHASE I""""

# # getting factors of a number 
# import logging
# logging.basicConfig(level = logging.DEBUG)
# def getFactors(number):
#     factors = [] # we are going to save factors into a blank list 
#     for potentialFactor in range (1, number +1 ): # for potentialFactor from 1 to including that number
#         if number % potentialFactor == 0:
#             factors.append(potentialFactor)
#     return factors
# logging.debug (getFactors(24))

# # DEBUG:root:[1, 2, 3, 4, 6, 8, 12, 24]


# """PHASE II We are going to find which of these numbers are prime numbers"""

# # getting factors of a number 
# import logging
# logging.basicConfig(level = logging.DEBUG)
# def getFactors(number):
#     factors = [] # we are going to save factors into a blank list 
#     for potentialFactor in range (1, number +1 ): # for potentialFactor from 1 to including that number
#         if number % potentialFactor == 0:
#             factors.append(potentialFactor)
#     return factors
# logging.debug (getFactors(17))

# # DEBUG:root:[1, 2, 3, 4, 6, 8, 12, 24]
# # determine if a number is prime
# def isPrime(number): #this is going to turn boolean true or false 
#     return len(getFactors(number)) == 2        #get that function and check if the length of that list returns is two or not
# # if it has two factors then that number is prime 
# logging.debug('isPrime(24) = %s'% (isPrime(24))) 
# #% means insert a value in the tuple that follows after the percent sign after this string right here
# logging.debug('isPrime(17) = %s' %(isPrime)(17))
# # DEBUG:root:isPrime(24) = False
# # DEBUG:root:isPrime(17) = True
# # find the highest number 

# """Get the factor of some numbers and go through those numbers and to see if they are prime or not"""
# # getting factors of a number 
# import logging
# logging.basicConfig(level = logging.DEBUG)
# def getFactors(number):
#     factors = [] # we are going to save factors into a blank list 
#     for potentialFactor in range (1, number +1 ): # for potentialFactor from 1 to including that number
#         if number % potentialFactor == 0:
#             factors.append(potentialFactor)
#     return factors
# logging.debug (getFactors(17))

# # DEBUG:root:[1, 2, 3, 4, 6, 8, 12, 24]
# # determine if a number is prime
# def isPrime(number): #this is going to turn boolean true or false 
#     return len(getFactors(number)) == 2        #get that function and check if the length of that list returns is two or not
# # if it has two factors then that number is prime 
# logging.debug('isPrime(24) = %s'% (isPrime(24))) 
# #% means insert a value in the tuple that follows after the percent sign after this string right here
# logging.debug('isPrime(17) = %s' %(isPrime)(17))
# # DEBUG:root:isPrime(24) = False
# # DEBUG:root:isPrime(17) = True
# allFactors =  getFactors(600851475143)
# # find the highest number  
# largestPrimeFactor = 0
# for factor in allFactors:
#     if isPrime(factor) and factor > largestPrimeFactor:
#         largetPrimeFactor = factor 
    
# print(largestPrimeFactor)

"""PHASE II We are going to find which of these numbers are prime numbers"""

# # getting factors of a number 
# import logging
# logging.basicConfig(level = logging.DEBUG)
# def getFactors(number):
#     factors = [] # we are going to save factors into a blank list 
#     for potentialFactor in range (1, int (number/2 +1) ): # for potentialFactor from 1 to including that number
#     # divide number by 2 so we only need to go through half of the number 
#         if number % potentialFactor == 0:
#             factors.append(potentialFactor)
#     return factors
# logging.debug (getFactors(17))

# # DEBUG:root:[1, 2, 3, 4, 6, 8, 12, 24]
# # determine if a number is prime
# def isPrime(number): #this is going to turn boolean true or false 
#     return len(getFactors(number)) == 2        #get that function and check if the length of that list returns is two or not
# # if it has two factors then that number is prime 
# logging.debug('isPrime(24) = %s'% (isPrime(24))) 
# #% means insert a value in the tuple that follows after the percent sign after this string right here
# logging.debug('isPrime(17) = %s' %(isPrime)(17))
# # DEBUG:root:isPrime(24) = False
# # DEBUG:root:isPrime(17) = True
# # find the highest number 

# """Get the factor of some numbers and go through those numbers and to see if they are prime or not"""
# # getting factors of a number 
# import logging
# import math
# logging.basicConfig(level = logging.DEBUG)
# def getFactors(number):
#     factors = [] # we are going to save factors into a blank list 
#     for potentialFactor in range (1, int(math.sqrt(number))+1 ): # for potentialFactor from 1 to including that number
#         if number % potentialFactor == 0:
#             factors.append(potentialFactor)
#             factors.append(number // potentialFactor) # we are getting 1 and 17 as the factors
#     return factors
# logging.debug (getFactors(17))

# # DEBUG:root:[1, 2, 3, 4, 6, 8, 12, 24]
# # determine if a number is prime
# def isPrime(number): #this is going to turn boolean true or false 
#     return len(getFactors(number)) == 2        #get that function and check if the length of that list returns is two or not
# # if it has two factors then that number is prime 
# logging.debug('isPrime(24) = %s'% (isPrime(24))) 
# #% means insert a value in the tuple that follows after the percent sign after this string right here
# logging.debug('isPrime(17) = %s' %(isPrime)(17))
# # DEBUG:root:isPrime(24) = False
# # DEBUG:root:isPrime(17) = True
# allFactors =  getFactors(600851475143)
# # find the highest number  
# largestPrimeFactor = 0
# for factor in allFactors:
#     if isPrime(factor) and factor > largestPrimeFactor:
#         largetPrimeFactor =+ factor 
# print(largestPrimeFactor)