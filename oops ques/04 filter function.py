# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 08:26:40 2024

@author: ADMIN
"""
# Illustration program that extracts only even number
# using Loops

def getEvennumber(numberlist):
    evennumberlist = []
    # A For loop is Employed to filtered Out list
    for number in numberlist:
        if number % 2 == 0:
            evennumberlist.append(number)
    return evennumberlist

numbers = [11,2,3,4,56,5,6,57,7]
even = getEvennumber(numbers)
print(even)
#*******************************************************
def isEven(x):
    if x % 2 ==0:
        return True
    else:
        return False
 
numbers = [1,2,3,4,5,6,8,10]
even = filter(isEven,numbers)

for e in even:
    print(e)


# *****************************************
# Filter out the vowels in the sequence
# *****************************************

def getVowel(x):
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    if x  in vowel:
        return True
    else:
        return False

stringinput =['h','o','w','w','o','n','d','e','r','f','u','l','l', 'I' ,'a', 'm']

filtered = filter(getVowel,stringinput)
print(list(filtered))


# **********************************************
#   Filters with Lambda function
#*********************************************

# Program to seperate odd and even numbers 
# into two different list
#***********************************************

#numbers = [1,2,3,4,5,6,7,8,9,10]
numbers= [1,3,5,7,9,10,100,1000,10000,100000]
oddnumbers = filter(lambda x: x%2 != 0,numbers)
print(list(oddnumbers))

evennumbers = filter(lambda x: x%2 == 0,numbers)
print(list(evennumbers))

#*************************************************

# Seperating Adult Customers and Children
#*********************************************
CustList = [["Anu",10],["Beena",18],["Citra",17],["Divya",45]]

def adultFilter(X):
    if X[1] >=18 :
        return True
    else:
        return False

adultlist = filter(adultFilter, CustList)
print(list(adultlist))

# Using Lambda function as predicate function
childrenlist = filter(lambda X : X[1] < 18,CustList)
print(list(childrenlist))