#!/usr/bin/python

import sys

num1 = 10
num2 = 2
try:
    num3 = num1/num2
    print("Execution of try block", num3)
except ZeroDivisionError as err:
    print("Error: {0}".format(err))
else:
    print("else block get executed")
finally:
    print("execution of the finally block")
