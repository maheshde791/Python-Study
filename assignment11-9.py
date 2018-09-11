# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:52:52 2018

@author: maheshde

Pythagoras theorem : Ass1
    c^2=a^2+b^2  (print 30 combinations of it)
    
    
    Try Use PEP8 coding standards
Ass2:
    Anagram
"""
import math

count = 0;
old_i = 0;

for hyp in range(1,100):
   for i in range(1,100):
       for j in range(1,100):
           if count <=30:
               if j != old_i: 
                   if hyp == math.sqrt(i**2 + j**2):
                       print("Combination count:",count,"hypo:",hyp,"=",i,"^2","*",j,"^2")
                       count+=1
                       old_i=i;
                       break