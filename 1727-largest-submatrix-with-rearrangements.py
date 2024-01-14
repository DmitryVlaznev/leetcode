# 1727. Largest Submatrix With Rearrangements

# Medium

# You are given a binary matrix matrix of size m x n, and you are
# allowed to rearrange the columns of the matrix in any order.

# Return the area of the largest submatrix within matrix where every
# element of the submatrix is 1 after reordering the columns optimally.


# Example 1:
# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.

# Example 2:
# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.

# Example 3:
# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns, and there
# is no way to make a submatrix of 1s larger than an area of 2.


# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m * n <= 10^5
# matrix[i][j] is either 0 or 1.

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cols_ones = [[0] * cols for _ in matrix]
        for i in range(cols):
            cols_ones[0][i] = matrix[0][i]

        for row in range(1, rows):
            for col in range(0, cols):
                if matrix[row][col] == 1:
                    cols_ones[row][col] = cols_ones[row - 1][col] + 1
                else:
                    cols_ones[row][col] = 0

        res = 0
        for row in range(rows):
            r = cols_ones[row][:]
            r.sort(reverse=True)
            h = float("inf")
            for col in range(cols):
                h = min(h, r[col])
                res = max(res, h * (col + 1))
        return res


s = Solution()
# [0, 0, 1]
# [1, 1, 1]
# [1, 0, 1]
s.largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]])
