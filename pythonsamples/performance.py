#!usr/bin/python
from timeit import Timer
def test_while():
    i = 0
    while i < 10:
    	print("value of i %d" %(i))
    	i += 1
    return
t = Timer(lambda: test_while())
print(t.timeit(number=1)) 