# 498. Diagonal Traverse

# Medium

# Given a matrix of M x N elements (M rows, N columns), return all
# elements of the matrix in diagonal order as shown in the below image.

# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]

# Output:  [1,2,4,7,5,3,6,8,9]

# Note:
# The total number of elements of the given matrix will not exceed
# 10,000.
from typing import List
from utils import checkList


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        counter, d, p, res = rows * cols, [-1, 1], [0, 0], []
        while counter > 0:
            counter -= 1
            res.append(matrix[p[0]][p[1]])
            q = [p[0] + d[0], p[1] + d[1]]
            if q[0] >= 0 and q[0] < rows and q[1] >= 0 and q[1] < cols:
                p = q
                continue
            d = [-1 * i for i in d]
            if p[0] == rows - 1 or (p[0] == 0 and p[1] < cols - 1):
                p[1] += 1
            else:
                p[0] += 1
        return res


# print(p, matrix[p[0]][p[1]])
t = Solution()

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
checkList([1, 2, 4, 7, 5, 3, 6, 8, 9], t.findDiagonalOrder(m))

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
checkList([1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12], t.findDiagonalOrder(m))

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
checkList([1, 2, 4, 7, 5, 3, 6, 8, 10, 11, 9, 12], t.findDiagonalOrder(m))

m = [[1, 2, 3]]
checkList([1, 2, 3], t.findDiagonalOrder(m))

m = [[1], [2], [3]]
checkList([1, 2, 3], t.findDiagonalOrder(m))

m = [[1]]
checkList([1], t.findDiagonalOrder(m))

m = []
checkList([], t.findDiagonalOrder(m))