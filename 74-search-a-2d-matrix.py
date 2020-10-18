# Search a 2D Matrix

# Write an efficient algorithm that searches for a value in an m x n
# matrix. This matrix has the following properties:
# * Integers in each row are sorted from left to right.
# * The first integer of each row is greater than the last integer of the previous row.


# Example 1:
# Input: matrix =
# [
#     [ 1, 3, 5, 7],
#     [10,11,16,20],
#     [23,30,34,50]
# ],
# target = 3
# Output: true

# Example 2:
# Input: matrix =
# [
#     [ 1, 3, 5, 7],
#     [10,11,16,20],
#     [23,30,34,50]
# ],
# target = 13
# Output: false

# Example 3:
# Input: matrix = [], target = 0
# Output: false


# Constraints:
# m == matrix.length
# n == matrix[i].length
# 0 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from typing import List
from utils import checkValue

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0: return False
        cols = len(matrix[0])
        if cols == 0: return False

        def flat_to_squared(index, cols):
            return index // cols, index % cols

        nums = rows * cols
        l = -1
        r = nums
        while r - l > 1:
            mid = l + (r - l) // 2
            row, col = flat_to_squared(mid, cols)
            if matrix[row][col] < target: l = mid
            else: r = mid
        if r == nums: return False
        row, col = flat_to_squared(r, cols)
        return matrix[row][col] == target

t = Solution()
checkValue(True, t.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
checkValue(True, t.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 50))
checkValue(True, t.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 10))
checkValue(False, t.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 60))
checkValue(False, t.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], -12))
checkValue(False, t.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13))
checkValue(False, t.searchMatrix([], 13))
checkValue(False, t.searchMatrix([[1]], 13))