# Number of Islands

# Given a 2d grid map of '1's (land) and '0's (water), count the number
# of islands. An island is surrounded by water and is formed by
# connecting adjacent lands horizontally or vertically. You may assume
# all four edges of the grid are all surrounded by water.

# Example 1:
# Input:
# 11110
# 11010
# 11000
# 00000
# Output: 1

# Example 2:
# Input:
# 11000
# 11000
# 00100
# 00011
# Output: 3

from typing import List


class Solution:
    def sink_island(self, row, col, rc, cc, grid):
        grid[row][col] = "0"
        if row > 0 and grid[row - 1][col] == "1":
            self.sink_island(row - 1, col, rc, cc, grid)
        if row < rc - 1 and grid[row + 1][col] == "1":
            self.sink_island(row + 1, col, rc, cc, grid)
        if col > 0 and grid[row][col - 1] == "1":
            self.sink_island(row, col - 1, rc, cc, grid)
        if col < cc - 1 and grid[row][col + 1] == "1":
            self.sink_island(row, col + 1, rc, cc, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rc = len(grid)
        if not rc: return 0
        cc = len(grid[0])
        if not cc: return 0

        for i in range(0, rc):
            for j in range(0, cc):
                if grid[i][j] == "1":
                    islands +=1
                    self.sink_island(i, j, rc, cc, grid)
        return islands

t = Solution()

input = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print("1 = ", t.numIslands(input))

input = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print("3 = ", t.numIslands(input))

input = [["0","0","0","0","0"],["0","0","0","0","0"]]
print("0 = ", t.numIslands(input))

input = [["1","1","0","1","0"]]
print("2 = ", t.numIslands(input))

input = [["1"],["1"],["0"],["1"],["0"]]
print("2 = ", t.numIslands(input))

input = [[]]
print("0 = ", t.numIslands(input))

input = []
print("0 = ", t.numIslands(input))
