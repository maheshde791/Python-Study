#! user/bin/python 

"""
basket = ['apple','orange','apple','pear']
fruit = set(basket)
print("set", fruit)

print("-"*80)

set1 = {1,2,3}
set2 = {4,5,3}
print("set1 union set2", set1.union(set2))
print("set1 intersection set2", set1.intersection(set2))
print(len(set1))
print("-" * 80)
"""
"""
items = set()

# Add three strings.
items.add("cat")
items.add("dog")
items.add("gerbil")
print(items)
"""

"""
print("-" * 80)
numbers1 = {1, 3, 5, 7}
numbers2 = {1, 3}

# Is subset.
if numbers2.issubset(numbers1):
    print("Is a subset")

# Is superset.
if numbers1.issuperset(numbers2):
    print("Is a superset")

print("-" * 80)
"""
"""
set1={3,45,344,66}
set2={1,44,66}
set3=set1.intersection(set2)
print("set1",set1)
print("set2",set2)
print("set3",set3)
print("-" * 80)
set1={3,45,344,66}
set2={1,44,66}
set1.intersection_update(set2)
print("set1",set1)
print("set2",set2)
print("-" * 80)
set1={3,45,344,66}
set2={1,44,66}
set3=set1.difference(set2)
print("set1 is different from set 2 and values are: ", set3)

print("-" * 80)
myset = set(['a','b','c'])
print("myset", myset)
myset.add('d')
print("updated myset", myset)
"""


#frozen set
frozen_set = frozenset(['e','f','g'])
print("frozen set",frozen_set)
#frozen_set.add('h')
#print(frozen_set)























