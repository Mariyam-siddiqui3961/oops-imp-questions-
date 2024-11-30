# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:51:00 2024

@author: ADMIN
"""
# List Comprehension
# Generration of Square values using list comprehension

sqrval = [x*x for x in range(10)]
print(sqrval)

# Generate a list of Even numbers from the given input list

inp = [0,1,2,3,4,5,6]

evnlist = [x for x in inp if x %2 ==0]
print(evnlist)

# Generator Comprehension
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_gen = (var for var in input_list if var % 2 == 0)

print("Output values using generator comprehensions:", end = ' ')

for var in output_gen:
	print(var, end = ' ')


# Set Comprehension
#Generate set of even numbers from the given list  using set comprehension 
inp = [1,2,2,3,3,3,4,4,4,5,6,7,7,8]
eveset = {x for x in inp if x % 2 ==0}
print(eveset)

# Dictionary Comprehension

val_cube = {val: val**3 for val in range(10)}
print(val_cube)