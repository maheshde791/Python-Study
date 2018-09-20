#! usr/bin/python

"""
g = lambda x: pow(x,2)
print(g(5))
"""

numbers = [x for x in range(1,51)]
print(numbers)
print("-"*80)


def sqr(x): return x ** 2
def cube(x): return (x**3)


#print(map(sqr,numbers))
#print("-"*80)



squares = map(lambda x: x*x, numbers)
print(squares)
print(list(squares))
print("-"*80)

"""
funcs = [sqr, cube]
for r in range(5):
	value = map(lambda x: x(r),funcs)
	print(value)

"""
"""
print("-"*80)
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(filter(lambda x: x in a, b))  # prints out [2, 3, 5, 7]
"""
"""
print("-"*80)
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
print(product)
"""
print("-"*80)
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)









