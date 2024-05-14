# 861. Score After Flipping Matrix

# Medium

# You are given an m x n binary matrix grid.

# A move consists of choosing any row or column and toggling each value
# in that row or column (i.e., changing all 0's to 1's, and all 1's to
# 0's).

# Every row of the matrix is interpreted as a binary number, and the
# score of the matrix is the sum of these numbers.

# Return the highest possible score after making any number of moves
# (including zero moves).


# Example 1:
# Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

# Example 2:
# Input: grid = [[0]]
# Output: 1


# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# grid[i][j] is either 0 or 1.

from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def ones_in_col(c):
            ones = 0
            for r in range(len(grid)):
                ones += grid[r][c]
            return ones

        def invert_col(c):
            for r in range(len(grid)):
                grid[r][c] = 0 if grid[r][c] == 1 else 1

        def invert_row(r):
            for c in range(len(grid[0])):
                grid[r][c] = 0 if grid[r][c] == 1 else 1

        def to_number(r):
            return int("".join(str(x) for x in grid[r]), 2)

        rows = len(grid)
        ones = ones_in_col(0)
        if ones < rows // 2 + rows % 2:
            invert_col(0)
        for r in range(rows):
            if grid[r][0] == 0:
                invert_row(r)
        for c in range(len(grid[0])):
            ones = ones_in_col(c)
            if ones < rows // 2 + rows % 2:
                invert_col(c)
        res = 0
        for r in range(rows):
            res += to_number(r)
        return res
