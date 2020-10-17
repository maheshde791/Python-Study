#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s.find('AM') != -1:
        if int(s[:2]) <= 11:
            return s[:8]
        elif int(s[:2]) == 12:
            return '00'+s[2:8]
    elif s.find('PM') != -1:
        if int(s[:2]) < 12:
            temp = int(s[:2]) + 12
            temp = str(temp)
            return temp+s[2:8]
        elif int(s[:2]) == 12:
            return s[0:8]
    #return '19:05:45'


if __name__ == '__main__':
    

    s = '12:01:00AM'

    result = timeConversion(s)
