# 542. 01 Matrix

# Medium

# for each cell.
# Given an m x n binary matrix mat, return the distance of the nearest 0

# The distance between two adjacent cells is 1.


# Example 1:
# Input: mat = [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]

# Example 2:
# Input: mat = [
#   [0,0,0],
#   [0,1,0],
#   [1,1,1]
# ]
# Output: [
#   [0,0,0],
#   [0,1,0],
#   [1,2,1]
# ]


# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

from typing import List
from collections import deque


class Solution:
    def visited(self, mi, ni, m, n, matrix):
        if mi < 0 or ni < 0 or mi >= m or ni >= n:
            return True
        return matrix[mi][ni] != None

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n, dq, d = len(mat), len(mat[0]), deque(), 0
        res = [[None] * n for _ in mat]

        for mi in range(m):
            for ni in range(n):
                if mat[mi][ni] == 0:
                    dq.append((mi, ni))
                    res[mi][ni] = d

        while dq:
            d += 1
            l = len(dq)
            while l:
                mi, ni = dq.popleft()
                for md, nd in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if not self.visited(mi + md, ni + nd, m, n, res):
                        res[mi + md][ni + nd] = d
                        dq.append((mi + md, ni + nd))
                l -= 1
        return res
