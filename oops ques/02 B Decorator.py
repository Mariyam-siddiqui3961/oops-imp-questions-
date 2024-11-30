# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:55:56 2024

@author: ADMIN
"""

def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")
    
# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()

#**************************************************
'''
Next example with @ Symbol
'''
#***************************************************
def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  


#**********************************************************
#  Deorator with arguments
#*********************************************************

def special_add(func):

    def inner(a,b,c):
        print("I got decorated by inner funtion")
        if c == 0:
            func(a,b,c)
        else:
            return func(2*a,2*b,c)
    return inner

@special_add
def ordinary_add(a,b,c):
    print(a+b)

ordinary_add(1,2,1)  
ordinary_add(1,2,0)

