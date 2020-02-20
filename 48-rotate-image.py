# 48. Rotate Image

# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Note:

# You have to rotate the image in-place, which means you have to modify
# the input 2D matrix directly. DO NOT allocate another 2D matrix and do
# the rotation.

# Example 1:

# Given input matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# Example 2:

# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],

# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n < 2:
            return

        for row in range(0, n):
            for col in range(0, n - 1 - row):
                matrix[row][col], matrix[n - 1 - col][n - 1 - row] = matrix[n - 1 - col][n - 1 - row], matrix[row][col]

        for row in range(0, n//2):
            opposite = n - 1 - row
            if opposite == row:
                break

            for col in range(0, n):
                matrix[row][col], matrix[opposite][col] = matrix[opposite][col], matrix[row][col]

test = Solution()
m = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
# s = [
#   [9,6,3],
#   [8,5,2],
#   [7,4,1]
# ]
s = [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

print("--------------")
print(s)
test.rotate(m)
print(m)
print("--------------")
print("")

m = [
  [ 1, 2, 3, 4],
  [ 5, 6, 7, 8],
  [ 9,10,11,12],
  [13,14,15,16]
]
# s = [
#   [16,12, 8, 4],
#   [15,11, 7, 3],
#   [14,10, 6, 2],
#   [13, 9, 5, 1]
# ]
s = [
  [13, 9, 5, 1],
  [14,10, 6, 2],
  [15,11, 7, 3],
  [16,12, 8, 4]
]
print("--------------")
print(s)
test.rotate(m)
print(m)
print("--------------")
print("")