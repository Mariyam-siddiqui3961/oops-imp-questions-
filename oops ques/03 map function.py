# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:56:44 2024

@author: ADMIN
"""

"""
map() function in python
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
Python map() Function Syntax
Syntax: map(fun, iter)
Parameters:
•	fun: It is a function to which map passes each element of given iterable.
•	iter: It is iterable which is to be mapped. (list, tuple)
NOTE: You can pass one or more iterable to the map() function
Returns: Returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .  
"""
# Normal Funtion Defined
def addition(n):
    return(n+n)
# A iterable object list is created
numbers = [1,2,3,4]
# map function applies the function to each element of the iterable object
doublenumbers = map(addition,numbers)
# the returned object is  map object
print(doublenumbers)
# map object is converted to list object
print(list(doublenumbers))


#****************************************
#   Map function with Lambda
#****************************************
numbers = [1,2,3,4]
result = map(lambda x:x*x,numbers)
print(list(result))

# Normal Function to square each element of a list
numbers = [1,2,3,4]
sqred = []
for num in numbers:
    sqred.append(num*num)
print(sqred)
#************************************************
# map function with more than one iterable objects

list1 = [1,2,3,4]
list2 = [5,6,7,8]

#Add Two Lists Using map and lambda

result = map(lambda x,y:x+y,list1,list2)

print(list(result))

#Write a python Program that doubles even numbers 
# in a list and keep odd numbers as such using map
# function


def double_even(x):
    if x % 2 == 0:
        return x*2
    else:
        return x

# create a list with odd and even numbers

list1 = [1,2,3,4,5,6,7]

result = map(double_even,list1)

print(list(result))