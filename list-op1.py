# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:32:00 2018

@author: maheshde
"""

items = [1,2,3,4,5]
squared = []
for i in items:
    squared.append(i**2)
    print(squared)
    
    
    #alist = ['a1', 'a2', 'a3']
    #for i, a in enumerate(alist)
    
    fz= frozenset(["mahesh","Shraddha","Mau"])
    print("Try to add element in frozen set:",fz)
    
    for x in range(10):
        print(x)
        
        #list compression
        x = [i for i in range(10)]
        print(x)
        
        square = [i*i for i in range(10)]
        print(square)