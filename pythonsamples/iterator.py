#!/usr/bin/python


str = "Welcome to Python"
"""
for i in str:
	print(i)

print("-"*80)
"""
"""
it = iter(str)

print(it.next())
print(it.next())


#print(it)
#print(list(it))

"""

def myGenerator():
	yield "These"
	yield "Words"
	yield "Come"
	yield "One"
	yield "At"
	yield "A"
	yield "Time"

myInstance = myGenerator()
print(myInstance.next())
print(myInstance.next())
myInstance1 = myGenerator()
print("-"*80)
print(myInstance1.next())
print(myInstance.next())


"""
for word in myInstance:
	print(word)
"""





