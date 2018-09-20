#! user/bin/python 

alist = ['a1', 'a2', 'a3']

for i, a in enumerate(alist):
    print i, a

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):
    print a, b


alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)

#map(function_to_apply, list_of_inputs)
#Most of the times we want to pass all the list elements to a function one-by-one and then collect the output. For instance:

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
print(squared)













items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

#Most of the times we use lambdas with map

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

#filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

#normal way
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
print(product)

#with reduce function
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


"""
print('-' * 80) 
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
print("list2[::-1]", list2[::-1])
print("list2[-2]", list2[-2])
list2.remove(6)
print("list2.remove", list2)

list3 = [0,1,2,3,4,5,6,7,8,9]
print("even numbers", list3[0::2])
print("Odd numbers", list3[1::2])
"""
"""
print('-' * 80)

list = ['physics', 'chemistry', 1997, 2000];

print("Value available at index 2 : ")
print(list[2])
list[2] = 2001;
print("New value available at index 2 : ")
print(list[2])
print('-' * 80) 
list1 = ['physics', 'chemistry', 1997, 2000];

print(list1)
del list1[2];
print("After deleting value at index 2 : ")
print(list1)
"""
"""
print('-' * 80)
list1, list2 = [123, 'xyz', 'zara'], [456, 13, 543]

print("First list length : ", len(list1))
print("Second list length : ", len(list2))

print("first list max:", max(list1))
print("Second list max:", max(list2))

print("first list min:", min(list1))
print("Second list min:", min(list2))
print('-' * 80)
"""
"""
aList = [123, 'xyz', 'zara', 'abc']
print("count the abc items : ", aList.count('abc'))
aList.append( 2009 )
print("append output - Updated List : ", aList)
aList.append('abc')
print("count the abc items : ", aList.count('abc'))
print("Index for xyz : ", aList.index('xyz')) 
print("List pop : ", aList.pop())
print("List pop 2 index: ", aList.pop(2))
aList.insert( 3, 'Cybage')
print('after insert list is', aList);
aList.reverse()
print("Reverse List : ", aList)
aList = [123, 'xyz', 'zara', 'abc', 'xyz']

aList.sort()
print("sort aList : ", aList)
print('-' * 80)

print(tuple(['pull request', 'open source', 'repository', 'branch']))
sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp']
print(tuple(sea_creatures))
print('-' * 80)

"""
"""
li = ['a', 'b', 'c']
li.extend(['d', 'e', 'f'])
print("extendlist", li)
li = ['a', 'b', 'c']
li.append(['d', 'e', 'f'])
print("appendlist", li)

"""
"""
l1 = [1,2,3,4,5,6,7,8,9]
for x in l1:
    print(x*x)
"""
"""


print("l1",l1)
print("x",x)    
"""






























































