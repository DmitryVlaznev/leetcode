# 54. Spiral Matrix

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        if rows == 0:
            return []

        cols = len(matrix[0])
        l = rows * cols

        res = [None] * l
        top = -1
        right = cols
        bottom = rows
        left = -1

        r = c = p = 0
        direction = "right"

        while p < l:
            res[p] = matrix[r][c]
            p = p + 1

            if direction == "right":
                if c + 1 < right:
                    c = c + 1
                else:
                    top = top + 1
                    r = r + 1
                    direction = "bottom"
            elif direction == "bottom":
                if r + 1 < bottom:
                    r = r + 1
                else:
                    right = right - 1
                    c = c - 1
                    direction = "left"
            elif direction == "left":
                if c - 1 > left:
                    c = c - 1
                else:
                    bottom = bottom - 1
                    r = r - 1
                    direction = "up"
            elif direction == "up":
                if r - 1 > top:
                    r = r - 1
                else:
                    left = left + 1
                    c = c + 1
                    direction = "right"

        return res

test = Solution()

m = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
res = [1,2,3,6,9,8,7,4,5]
print("--------------")
print(res)
print(test.spiralOrder(m))
print("--------------")
print("")

m = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
res = [1,2,3,4,8,12,11,10,9,5,6,7]
print("--------------")
print(res)
print(test.spiralOrder(m))
print("--------------")
print("")

print("--------------")
print([1])
print(test.spiralOrder([[1]]))
print("--------------")
print("")

print("--------------")
print([])
print(test.spiralOrder([[]]))
print("--------------")
print("")

print("--------------")
print([])
print(test.spiralOrder([]))
print("--------------")
print("")