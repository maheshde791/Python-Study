import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    # find possible combinations by clock wise rotate then reverse again rotate one answer magic matrix
    possible_combination = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        ]
    
    result_set = []
    for p in possible_combination:
        total = []
        total = [max([i,j]) - min([i,j]) for p_row, s_row in zip(p, s) for i, j in zip(p_row, s_row) if not i == j]
        result_set.append(sum(total))
    return min(result_set)
    #returning least cost moves to find magic no matrix

    
if __name__ == '__main__':
    
    s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

    result = formingMagicSquare(s)

