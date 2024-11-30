# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:26:35 2024

@author: ADMIN
"""
""" Example Program for Lambda Function
ananymous function with one or more arguments but one expression
"""

sqrVal = lambda x : x*x
print(sqrVal(4))

# sqrVal - Function Reference
# lambda - keyword
# x: x is arugument
# sigle expression x*x
# this expression value will be returned

"""  Example program for more than one arugumets   
     Distance between two points  x1,y1 and x2 and y2
"""
import math
distfunc = lambda x1,y1,x2,y2: math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
print(distfunc(0,0,0,4))

""" Lambda Function example """

uppercase = lambda text1: text1.upper()
uppercase("Galgotias University")

""" Why to use lambda function  
better as a ananymous funtion with in another function """

def multiplier (n):
    return lambda a: a*n

double = multiplier(2)
print("Double =" , double(3))

triple = multiplier(3)
print("Triple =" ,triple(5))

""" Difference between function and lambda function  """

def func_cube(x):
    return(x*x*x)

lambda_cube = lambda x: x*x*x

# invoking normal function

print(func_cube(4))

# invoking lambda function

print(lambda_cube(5))