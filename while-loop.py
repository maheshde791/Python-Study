# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:08:12 2018

@author: maheshde
"""

count =0
while count < 5:
    print(count)
    count += 1
    
    
#Continue statement,  will print odds
for x in range(10):
    if x%2 == 0:
        continue
    print(x)
    

#Break Statement use
players = ["Virat","Sachin","Laxman","Rahul"]
for player in players:
    print(player)
    if player == "Sachin":
        break
    
print("Aaj Rahul kitne no pr khelega:",players.count("Rahul"))
print("Aaj kon nahi khelega:",players.pop(3))
print(players.count("Rahul"))
print("Laxman Kitne no pr Aara:",players.index("Laxman")+1)
players.insert(2, "Dhoni") # location and Value
print("After insert:",players)
players.reverse()
print("In reverse:",players)

nos = [8,10,7,22]
players.append(nos)
print (players)


players = ["Virat","Sachin","Laxman","Rahul"]
nos = [8,10,7,22]
players.extend(nos)
print (players)

nums = [1,2,3,4,5,6,7,8,9]
print(nums[0::2])
