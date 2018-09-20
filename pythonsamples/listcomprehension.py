#! user/bin/python



"""
x = [i for i in range(10)]
print(x)


squares = []
for x in range(10):
    squares.append(x*x)
print("squares", squares)

squares = [n*2 for n in range(10)]
print("squares", squares)

"""
"""
l1 = [1,2,3,4,5,6,7,8,9]
x = [i for i in l1 if i%2 == 0]
print(x)
"""
"""
print("-" * 80)
originallist = ["A","B","C"]
newlist = [x.lower() for x in originallist]
print("originallist", originallist)
print("newlist", newlist)
"""
"""
a = [x.upper() for x in ["A","B","C"]]
print(a)
"""
"""
print("-"*80)
string = "Hello 12345 World 6789"
numbers = [x for x in string if x.isdigit()]
print(numbers)
print(type(numbers))
"""




"""
print("-"*80)
triple = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
print("Pythagorean triples", triple)
"""








"""
def checkAnagram(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(checkAnagram('heart','earth'))
#python typhon

"""































