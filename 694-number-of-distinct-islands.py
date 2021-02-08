# 694. Number of Distinct Islands

# Medium

# Given a non-empty 2D array grid of 0's and 1's, an island is a group
# of 1's (representing land) connected 4-directionally (horizontal or
# vertical.) You may assume all four edges of the grid are surrounded by
# water.

# Count the number of distinct islands. An island is considered to be
# the same as another if and only if one island can be translated (and
# not rotated or reflected) to equal the other.

# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.

# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.

# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered different island shapes, because we do not consider
# reflection / rotation.
# Note: The length of each dimension in the given grid does not exceed 50.

from typing import List
from utils import checkValue


class Solution:
    def dfs(self, grid, top, left, i, j, island):
        rows, cols = len(grid), len(grid[0])
        if 0 <= i < rows and 0 <= j < cols and grid[i][j]:
            grid[i][j] = 0
            island.append((i - top, j - left))
            neighbors = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
            for r, c in neighbors:
                self.dfs(grid, top, left, r, c, island)

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows, cols, islands = len(grid), len(grid[0]), set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    i0, j0, v = i, j, []
                    island = []
                    self.dfs(grid, i, j, i, j, island)
                    islands.add(tuple(island))
        return len(islands)


t = Solution()

grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
]
checkValue(1, t.numDistinctIslands(grid))

grid = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
]
checkValue(3, t.numDistinctIslands(grid))