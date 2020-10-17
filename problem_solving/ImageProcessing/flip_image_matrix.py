class Solution:
    def flip(self, matrix):
        #Received matrix rows in lists
        #print(*matrix)
        #Retrive and reverse each row (using list comprehension)
        #print([row[::-1] for row in matrix])
        #Use XOR operator to invert the values or use substraction with 1.
        #print([[val^1 for val in row[::-1]] for row in matrix])
        return [[1 - val for val in row[::-1]] for row in matrix]

obj1 = Solution()
print(obj1.flip([[1,1,0],[1,0,1],[0,0,0]]))