#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_height = max(candles)
    blow_candle = 0
    for hight in candles:
        if hight == max_height:
            blow_candle += 1
    return blow_candle

if __name__ == '__main__':

    candles = [3,2,1,6,3,6]

    result = birthdayCakeCandles(candles)
    print(result)
