import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    #ascii nos for a to z starts from 97
    map_dict = dict(zip([chr(i) for i in range(97, 123)], h))
    return max([map_dict[alphabate] for alphabate in word]) * len(word)

    


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #h = list(map(int, input().rstrip().split()))
    h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7] 
    word = 'ram'

    result = designerPdfViewer(h, word)

    #fptr.write(str(result) + '\n')

    #fptr.close()