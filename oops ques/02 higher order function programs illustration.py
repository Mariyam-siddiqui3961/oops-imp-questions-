# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:49:38 2024

@author: ADMIN
"""

# Python program to illustrate functions 
# can be treated as objects 

# Normal Function
def shout(text): 
	return text.upper() 
	
print(shout('Hello')) 
	
# Assigning function to a variable 
# a reference is created

yell = shout 
	
print(yell('Bacck backK')) 


###############################################################333
# Python program to illustrate functions 
# can be passed as arguments to other functions 

def shout(text): 
    return text.upper() 
	
def whisper(text): 
	return text.lower() 
	
def greet(func):   # Function is passes as a argument
	# storing the function in a variable 
	greeting = func("Hi, I am created by a function passed as an argument.") 
	print(greeting) 
	
greet(shout) 
#greet(whisper) 

#########################################################################3
# Python program to illustrate functions 
# Functions can return another function 
	
def create_adder(x): 
	def adder(y): 
		return x + y 
	
	return adder 
	
add_15 = create_adder(30) 
	
print(add_15(45)) 
#########################################################################3333
#          Function return another Function - Example
#####################################################################3
def multiplier (n):
    return lambda a: a*n

double = multiplier(2)
print("Double =" , double(3))

triple = multiplier(3)
print("Triple =" ,triple(5))

##########################################################################3