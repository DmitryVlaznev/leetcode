# 463. Island Perimeter

# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The
# grid is completely surrounded by water, and there is exactly one
# island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to
# the water around the island). One cell is a square with side length 1.
# The grid is rectangular, width and height don't exceed 100. Determine
# the perimeter of the island.


# Example:
# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

# Explanation: The perimeter is the 16 yellow stripes in the image below:

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def getNumberOfBorders(grid, r, c, rows, cols):
            n = 0
            if r == 0 or grid[r - 1][c] == 0: n += 1
            if r == rows - 1 or grid[r + 1][c] == 0: n += 1
            if c == 0 or grid[r][c - 1] == 0: n += 1
            if c == cols - 1 or grid[r][c + 1] == 0: n += 1
            return n

        def findIsland(grid, rows, cols):
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j]: return i, j
            return None, None

        rows, cols = len(grid), len(grid[0])
        r, c = findIsland(grid, rows, cols)
        if r is None: return 0

        from collections import deque
        q = deque()
        seen = set()
        q.append((r,c,))
        seen.add((r,c,))
        perimeter = 0

        while q:
            r, c = q.popleft()
            perimeter += getNumberOfBorders(grid, r, c, rows, cols)
            if r > 0 and grid[r - 1][c] == 1 and (r - 1, c,) not in seen:
                q.append((r - 1,c,))
                seen.add((r - 1,c,))
            if r < rows - 1 and grid[r + 1][c] == 1 and (r + 1, c,) not in seen:
                q.append((r + 1,c,))
                seen.add((r + 1,c,))

            if c > 0 and grid[r][c - 1] == 1 and (r, c - 1,) not in seen:
                q.append((r,c - 1,))
                seen.add((r,c - 1,))
            if c < cols - 1 and grid[r][c + 1] == 1 and (r, c + 1,) not in seen:
                q.append((r,c + 1,))
                seen.add((r,c + 1,))
        return perimeter


def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
log(16, t.islandPerimeter(grid))

grid = [[0,1,0,0]]
log(4, t.islandPerimeter(grid))

grid = [[0],[0],[0],[1]]
log(4, t.islandPerimeter(grid))

grid = [[0,0,0,0],
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]]
log(0, t.islandPerimeter(grid))

grid = [[1,1],[1,1],[1,1]]
log(10, t.islandPerimeter(grid))