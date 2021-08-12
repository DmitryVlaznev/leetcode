# 827. Making A Large Island

# Hard

# You are given an n x n binary matrix grid. You are allowed to change
# at most one 0 to be 1.

# Return the size of the largest island in grid after applying this
# operation.
# An island is a 4-directionally connected group of 1s.

# Example 1:
# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an
# island with area = 3.

# Example 2:
# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one
# island with area = 4.

# Example 3:
# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.

# Constraints:
# n == grid.length
# n == grid[i].length
# 1 <= n <= 500
# grid[i][j] is either 0 or 1.

from typing import List
from collections import defaultdict

from utils import checkValue

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        square = defaultdict(lambda: 0)
        island, n = 2, len(grid)
        square[0] = 0
        res = 0

        def isValid(i, j):
            nonlocal n
            if i < 0 or j < 0:
                return False
            if i >= n or j >= n:
                return False
            return True

        def isUnvisitedLand(i, j):
            return isValid(i, j) and grid[i][j] == 1

        def mark_island(i, j, island):
            steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for di, dj in steps:
                if isUnvisitedLand(i + di, j + dj):
                    square[island] += 1
                    grid[di + i][dj + j] = island
                    mark_island(i + di, j + dj, island)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    square[island] += 1
                    grid[i][j] = island
                    mark_island(i, j, island)
                    res = max(res, square[island])
                    island += 1

        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    continue

                largeSquare = 1
                seen = set()
                steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for di, dj in steps:
                    if isValid(i + di, j + dj) and grid[di + i][dj + j] not in seen:
                        largeSquare += square[grid[di + i][dj + j]]
                        seen.add(grid[di + i][dj + j])
                res = max(res, largeSquare)
        return res

s = Solution()


grid = [[1,0],[0,1]]
checkValue(3, s.largestIsland(grid))

grid = [[0,0],[0,0]]
checkValue(1, s.largestIsland(grid))

grid = [[0,1],[0,0]]
checkValue(2, s.largestIsland(grid))

grid = [[1,1],[1,0]]
checkValue(4, s.largestIsland(grid))

grid = [[1,1],[1,1]]
checkValue(4, s.largestIsland(grid))

grid = [[1]]
checkValue(1, s.largestIsland(grid))

grid = [[0]]
checkValue(1, s.largestIsland(grid))

grid = [[1,1,1],[1,0,1],[1,1,1]]
checkValue(9, s.largestIsland(grid))