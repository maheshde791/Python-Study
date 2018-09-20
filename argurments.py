# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 12:09:20 2018

@author: maheshde
"""

def test_var_args(farg, *args):
    print("fromal arg:",farg)
    for arg in args:
        print("Anather arg:",arg)
        
test_var_args(1,"two",3)

print("-"*80)

args=("two",3)

def test_var_args_call(arg1,arg2,arg3):
    print("arg1",arg1,"arg2",arg2,"arg3",arg3)
    
test_var_args_call(1,*args)

print("-"*80)