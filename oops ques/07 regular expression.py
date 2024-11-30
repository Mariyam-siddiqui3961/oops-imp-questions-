# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:57:03 2024

@author: ADMIN
"""
# Python library for regular expression
import re
text = "Hello Hello , I am selvi. My Mobile number is 9597387027  or 1234567890 and email ID kar@gmail.com"

# Litteral pattern match to match 'selvi'
pattern1 = 'selvi'
patternfound = re.findall(pattern1, text)
print(patternfound)

# character class pattern to find vowels
pattern2  = "[aeiouAEIOU]"
charClassPatternFound = re.findall(pattern2, text)
print(charClassPatternFound)

#Qualifier Pattern a{3} exactly three consequtive a's
QualifierPattern = "l{2}"
PatternFound  = re.findall(QualifierPattern, text)
print(PatternFound)

# Alternative pattern
AlternativePattern = "Mobile|mobile|mob|Mob"
patternFound = re.findall(AlternativePattern,text)
print(patternFound)

#Grouping pattern Finding accourances of one or more sequences
GrpPattern = "(Hello)+"
patternFound = re.findall(GrpPattern,text)
print(patternFound)

# Regular expression for getting mobile number (10 Digits)
mobnumpattern = r"[0-9]{10}\b"
patternFound = re.findall(mobnumpattern,text)
print(patternFound)


