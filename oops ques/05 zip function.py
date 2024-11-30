# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:16:21 2024

@author: ADMIN
"""

fName = ['selvi','dev','kavi']
lName= ['subra','gupta','verma']
mapped  = zip(fName,lName)
print(list(mapped))

rollNo = (0x1,0x2,0x3,0x4)
Name  = ("aman","Binku","Chitu")
mapped1 = zip(rollNo,Name)
print(set(mapped1))


# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]

# printing players and scores.
for pl, sc in zip(players, scores):
	print("Player : %s	 Score : %d" % (pl, sc))
