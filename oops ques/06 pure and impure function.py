# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:22:01 2024

@author: ADMIN
"""
# Pure Function
# No side Effects

def pfun(a,b):
    return((a*b)/a)

# impure Function 
# Mofifying Global vaiable
global denominator
denominator = 7
def impfun(a,b):
    return ((a*b)/denominator)
print(impfun(3,4))
denominator = 6
print(impfun(3,4))

# impure Function
# function receives input
def impfun1(a,b):
    denominator = int(input("Enter Denominator"))
    return ((a*b)/denominator)
print(impfun1(3,4))
print(impfun1(3,4))

# impure Function - Random number
import random
def diceRoll():
    return(random.randint(1,6))
