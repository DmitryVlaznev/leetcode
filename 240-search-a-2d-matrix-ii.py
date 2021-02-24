# 240. Search a 2D Matrix II

# Medium

# Write an efficient algorithm that searches for a target value in an m
# x n integer matrix. The matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.


# Example 1:
# Input: matrix = [
#   [1,4,7,11,15],
#   [2,5,8,12,19],
#   [3,6,9,16,22],
#   [10,13,14,17,24],
#   [18,21,23,26,30]
# ], target = 5
# Output: true

# Example 2:
# Input: matrix = [
#   [1,4,7,11,15],
#   [2,5,8,12,19],
#   [3,6,9,16,22],
#   [10,13,14,17,24],
#   [18,21,23,26,30]
# ], target = 20
# Output: false

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matix[i][j] <= 10^9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10^9 <= target <= 10^9

from typing import List
from utils import checkValue


class Solution:
    # O(min(n,m) * log max(n,m)) solution
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        from bisect import bisect_left

        if m <= n:
            for r in matrix:
                i = bisect_left(r, target)
                if i < n and r[i] == target:
                    return True
        else:

            class ColumnWrapper:
                def __init__(self, matrix, column):
                    self.matrix = matrix
                    self.column = column

                def __getitem__(self, i):
                    return self.matrix[i][self.column]

                def __len__(self):
                    return len(self.matrix)

            for c in range(len(matrix[0])):
                i = bisect_left(ColumnWrapper(matrix, c), target)
                if i < m and matrix[i][c] == target:
                    return True

        return False

    # O(n + m) solution
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = m - 1, 0
        while c < n and r >= 0:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True
        return False


t = Solution()

m = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
checkValue(True, t.searchMatrix(m, 5))
checkValue(True, t.searchMatrix2(m, 5))

m = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
checkValue(False, t.searchMatrix(m, 20))
checkValue(False, t.searchMatrix2(m, 20))

m = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17],
    [18, 21, 23, 26],
]
checkValue(True, t.searchMatrix(m, 14))
checkValue(True, t.searchMatrix2(m, 14))

m = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17],
    [18, 21, 23, 26],
]
checkValue(False, t.searchMatrix(m, 15))
checkValue(False, t.searchMatrix2(m, 15))