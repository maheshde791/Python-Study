#See doc wordfile in same  directory
from collections import defaultdict
class Solution:
    def largestOverlap(self, img1, img2):
        dim = len(img1)
        #print(dim)

        def non_zero_cells(in_mat):
            return [(i,j) for i in range(dim) for j in range(dim) if in_mat[i][j] == 1]

        img1_ones = non_zero_cells(img1)
        img2_ones = non_zero_cells(img2)
        print("image1 ones: ", img1_ones)
        print("image2 ones: ", img2_ones)

        transformation_count = defaultdict(int)
        max_overlaps = 0
        #print(transformation_count)
        for (x_a, y_a) in img1_ones:
            for (x_b, y_b) in img2_ones:
                vec = (x_b - x_a, y_b - y_a)
                transformation_count[vec] += 1
                #print(transformation_count)
                max_overlaps = max(max_overlaps, transformation_count[vec])
        return max_overlaps


obj1 = Solution()
print(obj1.largestOverlap([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]))