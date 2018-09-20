# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 11:45:45 2018

@author: maheshde

Functions
Need to correct this program
"""

def changeme(mylist):
    mylist.append([1,2,3,4])
    print("Value inside the function:",mylist)
    return

#call 
    mylist = [10,20,30]
    changeme(mylist)
    print("Value outside the function:",mylist)
