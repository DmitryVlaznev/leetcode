# 73. Set Matrix Zeroes

# Given a m x n matrix, if an element is 0, set its entire row and
# column to 0. Do it in-place.

# Example 1:

# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:

# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]

# Follow up:
# * A straight forward solution using O(mn) space is probably a bad
#   idea.
# * A simple improvement uses O(m + n) space, but still not the best
#   solution.
# * Could you devise a constant space solution?

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        fillFirstRow = False
        fillFirstCol = False
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(0, rows):
            for c in range(0, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

                    fillFirstRow = True if fillFirstRow or r == 0 else False
                    fillFirstCol = True if fillFirstCol or c == 0 else False

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if fillFirstRow:
            for c in range(0, cols):
                matrix[0][c] = 0

        if fillFirstCol:
            for r in range(0, rows):
                matrix[r][0] = 0

test = Solution()
m = [[1,1,1], [1,0,1], [1,1,1]]
s = [[1,0,1], [0,0,0], [1,0,1]]

print("--------------")
print(s)
test.setZeroes(m)
print(m)
print("--------------")
print("")

m = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
s = [[0,0,0,0], [0,4,5,0], [0,3,1,0]]

print("--------------")
print(s)
test.setZeroes(m)
print(m)
print("--------------")
print("")

m = [[7,1,2,0], [0,4,5,2], [1,3,1,5]]
s = [[0,0,0,0], [0,0,0,0], [0,3,1,0]]

print("--------------")
print(s)
test.setZeroes(m)
print(m)
print("--------------")
print("")