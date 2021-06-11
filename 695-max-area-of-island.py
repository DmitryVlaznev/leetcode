# 695. Max Area of Island

# Medium

# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or
# vertical.) You may assume all four edges of the grid are surrounded by
# water.

# The area of an island is the number of cells with a value 1 in the
# island.

# Return the maximum area of an island in grid. If there is no island,
# return 0.

# Example 1:
# Input: grid = [
# [0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]
# ]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(i, j):
            square = 1
            grid[i][j] = 0
            if i > 0 and grid[i - 1][j] == 1:
                square += explore(i - 1, j)
            if i < len(grid) - 1 and grid[i + 1][j] == 1:
                square += explore(i + 1, j)
            if j > 0 and grid[i][j - 1] == 1:
                square += explore(i, j - 1)
            if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                square += explore(i, j + 1)
            return square

        res = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, explore(i, j))
        return res