#! user/bin/python
#from __future__ import division
"""
a = 9
b = 2
print("a/b", a/b)
print("a//b", a//b)
a = -9
print("a/b", a/b)
print("a//b", a//b)
print("-" * 80)

a = 9.5
b = 2
print("a/b", a/b)
print("a//b", a//b)
"""
"""
print("-" * 80)
print("Exponent of 2 and 3", 2**3)
print("pow(2,3)", pow(2,3))
print("mod of 5 and 2", 5%2)
"""
"""
print("-" * 80)

a = 10
b = 0
if (a and b):
	print("Yes")
else:
	print("No")
print('-' * 80)

"""
#MEMBER OPERATOR
print("MEMBER OPERATOR")
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print("Line 1 - a is available in the given list")
else:
   print("Line 1 - a is not available in the given list")

"""
if ( b not in list ):
   print("Line 2 - b is not available in the given list")
else:
   print("Line 2 - b is available in the given list")
"""
a = 2
if ( a in list ):
   print("Line 3 - a is available in the given list")
else:
   print("Line 3 - a is not available in the given list")

print('-' * 80)
print ('IDENTITY OPERATOR')
#IDENTITY OPERATOR

a = 20
b = 20

if ( a is b ):
   print("Line 1 - a and b have same identity")
else:
   print("Line 1 - a and b do not have same identity")

if ( id(a) == id(b) ):
   print("Line 2 - a and b have same identity", id(a), id(b))
else:
   print("Line 2 - a and b do not have same identity")

b = 30
if ( a is b ):
   print("Line 3 - a and b have same identity")
else:
   print("Line 3 - a and b do not have same identity")

if ( a is not b ):
   print("Line 4 - a and b do not have same identity")
else:
   print("Line 4 - a and b have same identity")

print('-' * 80)
print ('BINARY OPERATOR')
#BINARY OPERATOR
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print("Binary a and b ", c)

c = a | b;        # 61 = 0011 1101 
print("Binary a or b - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print("Binary XOR - Value of c is ", c)


c = a << 2;       # 240 = 1111 0000
print("Binary Left Shift- Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print("Binary Right Shift- Value of c is ", c)
"""
