# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 12:23:17 2018

@author: maheshde
"""

#import sys

num1 = 10
num2 = 2

try:
    num3 = num1/num2
    print("Execution of try block",num3)
except ZeroDivisionError as err:
    print("Error: {0}".format(err))
else:
    print("Else block get executed")
finally:
    print("Finally gets exec")