# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:40:07 2018

@author: maheshde
"""

list = ['Apple',25,'Banana',5]

print("Printing list :",list)
list.append('Cherry')
print("Printing list :",list)
list.reverse()
print("Printing list :",list)
list.remove('Apple')
print("Printing list :",list)

print(type(list))

dict = {'name':'xyz','Address':'Alibaug'}
print("Printing Dictonary:",dict)

del dict['Address']

print("Printing Dictonary:",dict)
#print( dict.value())