
import math
import os
import random
import re
import sys



#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    # Write your code here
    result = []
    for item in query:
        c = 0
        for item2 in dictionary:
            if sorted(item) == sorted(item2):
                #print(item)
                c += 1
        result.append(c)
    return result
        




                

if __name__ == '__main__':

    result = stringAnagram(['listen', 'tow', 'silent', 'lisent', 'two', 'abc', 'no', 'on'], ['two', 'bca', 'no', 'listen'])
    print(result)
    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()