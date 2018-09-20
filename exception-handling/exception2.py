# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 12:35:04 2018

@author: maheshde
"""

def has_even_number(l):
    for ele in l:
        if ele % 2 == 0:
            print("List contains an even number")
            break
        
        #This else will execute only when breakis never
        #reached out loop and terminated after all iterations
    else:
        print("List does not contain an even no")
        
#Driver code
print("For list 1:")
has_even_number([1,3,5,7,8])
print("\nFor list 2:")
has_even_number([1,3,5])