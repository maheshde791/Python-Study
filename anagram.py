# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:11:00 2018

@author: maheshde
"""

str1 = input("Enter String 1:")
str2 = input("Enter String 2:")

if(sorted(str1) == sorted(str2)):
    print("The string are Anagrams")
else:
    print("Strings are not Anagrams")