#!usr/bin/python
#list
numbers = [1,2,3,4,5,6]
print([x*x for x in numbers])
print("-"*80)
#set
numbers = [5,4,3]
print({x*x for x in numbers})
print("-"*80)
#dic
numbers = [1,2,3,4,5,6]
print({x:x*x for x in numbers})
print("-"*80)

#generators
numbers = [1,2,3,4,5,6]
lazy_squares = (x*x for x in numbers)
print(lazy_squares.next())