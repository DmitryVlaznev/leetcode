# 1102. Path With Maximum Minimum Value

# Medium

# Given an m x n integer matrix grid, return the maximum score of a path
# starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4
# cardinal directions.

# The score of a path is the minimum value in that path.

# For example, the score of the path 8 → 4 → 5 → 9 is 4.


# Example 1:
# Input: grid = [
#   [5,4,5],
#   [1,2,6],
#   [7,4,6]
# ]
# Output: 4
# Explanation: The path with the maximum score is highlighted in yellow.

# Example 2:
# Input: grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
# Output: 2

# Example 3:
# Input: grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
# Output: 3

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# 0 <= grid[i][j] <= 10^9

from typing import List
import heapq


class UnionFind:
    def __init__(self, size):
        self.parents = list(range(size))

    def union(self, a, b):
        self.parents[self.find(a)] = self.parents[self.find(b)]

    def find(self, a):
        while self.parents[a] != a:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def to_flat(r, c):
            return r * cols + c

        hq = []
        for r in range(rows):
            for c in range(cols):
                heapq.heappush(hq, (-1 * grid[r][c], r, c))

        visited, uf = set(), UnionFind(rows * cols)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while hq:
            value, r, c = heapq.heappop(hq)
            visited.add(to_flat(r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                if to_flat(nr, nc) in visited:
                    uf.union(to_flat(r, c), to_flat(nr, nc))
            if uf.find(0) == uf.find(rows * cols - 1):
                return abs(value)


s = Solution()

grid = [[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]
print(s.maximumMinimumPath(grid))
