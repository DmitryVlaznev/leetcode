# 417. Pacific Atlantic Water Flow

# Medium

# Given an m x n matrix of non-negative integers representing the height
# of each unit cell in a continent, the "Pacific ocean" touches the left
# and top edges of the matrix and the "Atlantic ocean" touches the right
# and bottom edges.

# Water can only flow in four directions (up, down, left, or right) from
# a cell to another one with height equal or lower.

# Find the list of grid coordinates where water can flow to both the
# Pacific and Atlantic ocean.

# Note:

# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.

# Example:
# Given the following 5x5 matrix:

#   Pacific ~   ~   ~   ~   ~
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic

# Return:

# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions
# with parentheses in above matrix).

from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def can_flow(i_fr, j_fr, i_to, j_to):
            if i_fr < 0 or j_fr < 0 or i_fr >= len(matrix) or j_fr >= len(matrix[0]):
                return False
            return matrix[i_fr][j_fr] >= matrix[i_to][j_to]

        def dfs(i, j, seen):
            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in d:
                if can_flow(i + dr, j + dc, i, j) and (i + dr, j + dc) not in seen:
                    seen.add((i + dr, j + dc))
                    dfs(i + dr, j + dc, seen)

        rows = len(matrix)
        if not rows:
            return []
        cols = len(matrix[0])
        if not cols:
            return []

        pacific, atlantic = set(), set()

        for i in range(rows):
            pacific.add((i, 0))
            dfs(i, 0, pacific)
            atlantic.add((i, cols - 1))
            dfs(i, cols - 1, atlantic)

        for j in range(cols):
            pacific.add((0, j))
            dfs(0, j, pacific)
            atlantic.add((rows - 1, j))
            dfs(rows - 1, j, atlantic)

        return [list(idx) for idx in pacific.intersection(atlantic)]


t = Solution()

m = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(t.pacificAtlantic(m))

m = [[1, 2, 2, 3, 5]]
print(t.pacificAtlantic(m))

m = [
    [1],
    [3],
    [2],
    [6],
    [5],
]
print(t.pacificAtlantic(m))

m = [
    [2, 2],
    [2, 2],
    [2, 2],
]
print(t.pacificAtlantic(m))

m = [
    [2, 2, 2],
    [2, 2, 2],
]
print(t.pacificAtlantic(m))

m = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
]
print(t.pacificAtlantic(m))

m = []
print(t.pacificAtlantic(m))

m = [[]]
print(t.pacificAtlantic(m))

m = [[1]]
print(t.pacificAtlantic(m))