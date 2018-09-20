# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 11:41:33 2018

@author: maheshde
pythagoras
"""

triple = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
print("Pythagoras triples",triple)