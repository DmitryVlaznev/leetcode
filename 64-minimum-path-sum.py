# Minimum Path Sum

# Given a m x n grid filled with non-negative numbers, find a path from
# top left to bottom right which minimizes the sum of all numbers along
# its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

from typing import List

class Solution:
    def print_route(self, route, grid):
        rows = len(grid)
        cols = len(grid[0])
        path = []
        for i in range(0, rows): path.append([" "] * cols)

        r = rows - 1
        c = cols - 1
        path[0][0] = str(grid[0][0])
        path[r][c] = str(grid[r][c])
        while route[(r, c)] != None:
            r, c = route[(r, c)]
            path[r][c] = str(grid[r][c])

        print("----------------")
        for i in range(0, rows): print(path[i])
        print("----------------")

    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if not rows: return 0
        cols = len(grid[0])
        if not cols : return 0

        import heapq

        h = []
        heapq.heappush(h, (grid[0][0], (0, 0)))
        visited = set()
        visited.add((0, 0))

        while True:
            path, coords = heapq.heappop(h)
            row, col = coords
            if row == rows - 1 and col == cols - 1: return path

            if row < rows - 1 and (row + 1, col) not in visited:
                visited.add((row + 1, col))
                heapq.heappush(h, (path + grid[row + 1][col], (row + 1, col)))
            if col < cols - 1 and (row, col + 1) not in visited:
                visited.add((row, col + 1))
                heapq.heappush(h, (path + grid[row][col + 1], (row, col + 1)))

    # Full A* search with any possible direction
    def minPathSumAStar(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if not rows: return 0
        cols = len(grid[0])
        if not cols : return 0

        import heapq

        h = []
        heapq.heappush(h, (grid[0][0], (0, 0)))
        visited = set()
        visited.add((0, 0))

        route = {}
        route[(0, 0)] = None
        while True:
            path, coords = heapq.heappop(h)
            row, col = coords
            if row == rows - 1 and col == cols - 1:
                self.print_route(route, grid)
                return path

            if row > 0 and (row - 1, col) not in visited:
                visited.add((row - 1, col))
                heapq.heappush(h, (path + grid[row - 1][col], (row - 1, col)))
                route[(row - 1, col)] = (row, col)
            if row < rows - 1 and (row + 1, col) not in visited:
                visited.add((row + 1, col))
                heapq.heappush(h, (path + grid[row + 1][col], (row + 1, col)))
                route[(row + 1, col)] = (row, col)
            if col > 0 and (row, col - 1) not in visited:
                visited.add((row, col - 1))
                heapq.heappush(h, (path + grid[row][col - 1], (row, col - 1)))
                route[(row, col - 1)] = (row, col)
            if col < cols - 1 and (row, col + 1) not in visited:
                visited.add((row, col + 1))
                heapq.heappush(h, (path + grid[row][col + 1], (row, col + 1)))
                route[(row, col + 1)] = (row, col)


t = Solution()
input = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print("7 = ", t.minPathSum(input))

input = [[42]]
print("42 = ", t.minPathSum(input))

input = [[]]
print("0 = ", t.minPathSum(input))

input = [
    [5,4,2,9,6,0,3,5,1,4,9,8,4,9,7,5,1],
    [3,4,9,2,9,9,0,9,7,9,4,7,8,4,4,5,8],
    [6,1,8,9,8,0,3,7,0,9,8,7,4,9,2,0,1],
    [4,0,0,5,1,7,4,7,6,4,1,0,1,0,6,2,8],
    [7,2,0,2,9,3,4,7,0,8,9,5,9,0,1,1,0],
    [8,2,9,4,9,7,9,3,7,0,3,6,5,3,5,9,6],
    [8,9,9,2,6,1,2,5,8,3,7,0,4,9,8,8,8],
    [5,8,5,4,1,5,6,6,3,3,1,8,3,9,6,4,8],
    [0,2,2,3,0,2,6,7,2,3,7,3,1,5,8,1,3],
    [4,4,0,2,0,3,8,4,1,3,3,0,7,4,2,9,8],
    [5,9,0,4,7,5,7,6,0,8,3,0,0,6,6,6,8],
    [0,7,1,8,3,5,1,8,7,0,2,9,2,2,7,1,5],
    [1,0,0,0,6,2,0,0,2,2,8,0,9,7,0,8,0],
    [1,1,7,2,9,6,5,4,8,7,8,5,0,3,8,1,5],
    [8,9,7,8,1,1,3,0,1,2,9,4,0,1,5,3,1],
    [9,2,7,4,8,7,3,9,2,4,2,2,7,8,2,6,7],
    [3,8,1,6,0,4,8,9,8,0,2,5,3,5,5,7,5],
    [1,8,2,5,7,7,1,9,9,8,9,2,4,9,5,4,0],
    [3,4,4,1,5,3,3,8,8,6,3,5,3,8,7,1,3]
]

print("82 = ", t.minPathSum(input))