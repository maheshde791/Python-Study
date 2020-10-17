class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        """ Given matrix : rotate 90* clock-wise
            |1,2,3|
            |4,5,6|
            |7,8,9]
            using zip() function to map or group similar index 
            elements of multiple containers(list in our case).
            So that we can transpose matrix and reverse each 
            row elements to get output.
        """
        #This will do transpose given matrix, zip obj printed as list
        #print(list(zip(*matrix)))
        #here matrix is reordered in reverse [<start>:<end>:<step>(order negative-index)]
        #using slice operator
        #print(map(list, zip(*matrix[::-1])))
        #To print it 
        #print(list(map(list, zip(*matrix[::-1]))))

        #final output
        matrix = map(list, zip(*matrix[::-1]))

obj1 = Solution()
obj1.rotate([[1,2,3],[4,5,6],[7,8,9]])