# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:44:56 2024

@author: ADMIN
"""
# iteralble list object
list1 = [45,67,85,90,100]

# converting to iterator using iter fucntion

myiterator = iter(list1)

print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))
print(next(myiterator))

# ****************************************************
# Write a Program to create a list with sqr values 
# of the given list using iterator funtion
#*****************************************************

list2  = [ 1,3,5,7,9]
listiteratator = iter(list2)

n = len(list2)
sqrlist = []

for i in range(n):
    x = next(listiteratator)
    sqrlist.append(x*x)
print(sqrlist)

#*******************************************************
# String Iterator
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""
# String values are iterable
mystr = "banana"
# an iterator is created using iter function

myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#**********************************************************
#Create an iterator object that produces the fibbanoci sequence
#**************************************************************
class Fibbanoci:
    # Constuctor function that initialize the seed values
    def __init__(self,s1 = 0,s2 = 1):
        self.count = 0
        self.s1 = s1
        self.s2 = s2
    # iter function do operations and return object itself
    def __iter__(self):
        return(self)       
    # implementation of next function that returns the next element in fibanoci sequence
    def __next__(self):
        if self.count == 0:
            self.count += 1
            return(self.s1)
        if self.count == 1:
            self.count += 1
            return(self.s2)
        if self.count>1:
            self.count +=1
            self.fib = self.s1+self.s2
            self.s1 = self.s2
            self.s2 = self.fib
            return(self.fib)
# Creating an Object for Fibanoci class which implements both iter and next method to create an iterator object        
fib1 = Fibbanoci(0,1)
# An iterator object is created using iter method
fib_iter = iter(fib1)
# Next element in the iterable object is produced
print(next(fib_iter))

fib2 = Fibbanoci(3,4)
fib_iter2 = iter(fib2)
print(next(fib_iter2))
        
#**********************************************************
#Create an iterator object that produces the fibbanoci sequence and Sequence terminates 
# after generating 10 numbers by raise  stop iteration
#**************************************************************
class Fibbanoci:
    # Constuctor function that initialize the seed values
    def __init__(self,s1 = 0,s2 = 1):
        self.count = 0
        self.s1 = s1
        self.s2 = s2
      
    # iter function do operations and return object itself
    def __iter__(self):
        return(self)       
    # implementation of next function that returns the next element 
    # in fibanoci sequence
    def __next__(self):
        if self.count < 10:
            if self.count == 0:
                self.count += 1
                return(self.s1)
            if self.count == 1:
                self.count += 1
                return(self.s2)
            if self.count>1:
                self.count +=1
                self.fib = self.s1+self.s2
                self.s1 = self.s2
                self.s2 = self.fib
                return(self.fib)
        else:
            raise StopIteration
        
fib1 = Fibbanoci(0,1)
fib_iter = iter(fib1)
print(next(fib_iter))

#*****************************************************************************
# Finding factors of n using generator
#****************************************************************************
def factors(n):
  for val in range(1, n+1):
      if n % val == 0:
          yield val
# No return statemnet in the above function
# we have yield statement in function that makes it as generator
# lazy evaluation - generates the factors only when required on the fly
# Not stored all the factors
   
# Geneartor object created 
factors_of_20 = factors(20)
# Produce the values when needed
print(next(factors_of_20))

"""
1
"""
#*******************************************************************************

# Generators for Fibbanoci Sequence
def Fibba ():
    a,b = 0,1
    while True:
        yield a
        a ,b = b, a+b
#create a generator to produce fib numbers

fib_gen  = Fibba()

# Generate and print first 10 fibbanoci numbers

for i in range(10):
    print(next(fib_gen))
    