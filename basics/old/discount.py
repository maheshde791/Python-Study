# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 13:41:35 2018

@author: maheshde
Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?

"""

bookprice = 24.95
discountedp = bookprice-(0.4*bookprice)
print(discountedp) #discounted price of a book

#shipping cost
firstcopy = 3
rest = 0.75
ordercopy = 60

total = (discountedp*ordercopy)+firstcopy+(rest*ordercopy-1)
print (total)  