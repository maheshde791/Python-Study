#!usr/bin/python
from timeit import Timer

"""
def createGenerator():
    mylist = range(4)
    for i in mylist:
        yield i
        
mygenerator = createGenerator()
for i in mygenerator:
    print(i)        
"""




#store all the values in memory

def simpleloop():
	mylist = [0, 1, 2, 3]
	for i in mylist:
		print i

t = Timer(lambda: simpleloop())
print t.timeit(number=1) 


#store all the values in memory
print "-" * 80

"""
mylist = [x*x for x in range(3)]
for i in mylist:
    print i	
print "-" * 80
"""


