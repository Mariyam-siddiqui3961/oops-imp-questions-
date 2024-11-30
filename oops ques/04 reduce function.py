# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:04:36 2024

@author: ADMIN
"""
# importing reduce function frm functtools module
from functools import reduce
#Pre defined Function
# takes two arguments and produce one value
# here two arguments are x & y
# one output is x+y
def sumxy(x,y):
    return(x+y)
# an Iterable to which function is applied
l1= [1,2,3,4,5,6,7]
# Reduce Function to sum up all elements of list
# using sum of 2 numbers function

cummulativesum = reduce(sumxy,l1)
# printing the generated single valued results
print(cummulativesum)

#*************************************************
# use reduce function to find min of given list
#*************************************************
from functools import reduce
def minxy(x,y):
    if x>y: 
        return y
    else:
        return x  
l1 = [8,3,5,-126,2,0,-134,4,]
# reduce function with three arguments
# third argument is initializer value for 
# first argument (ccumulative Value)
print(reduce(minxy,l1,0))
l2  = [5,6,7,2,4]
print(reduce(minxy,l2,0))
#******************************************************

# Reduce function with Lambda

l1  = [1,2,3,4,10]
product  = reduce(lambda x,y: x*y,l1)
print(product)