# 329. Longest Increasing Path in a Matrix

# Hard

# Given an m x n integers matrix, return the length of the longest
# increasing path in matrix.

# From each cell, you can either move in four directions: left, right,
# up, or down. You may not move diagonally or move outside the boundary
# (i.e., wrap-around is not allowed).


# Example 1:
# Input: matrix =
# [
#     [9,9,4],
#     [6,6,8],
#     [2,1,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

# Example 2:
# Input: matrix =
# [
#     [3,4,5],
#     [3,2,6],
#     [2,2,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving
# diagonally is not allowed.

# Example 3:
# Input: matrix = [[1]]
# Output: 1


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 231 - 1

from typing import List
from utils import checkValue


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dag = [0] * (rows * cols)
        t_sorted = []

        def siblings(i, reversed=False):
            nonlocal rows, cols
            r, c = i // cols, i % cols
            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            res = []
            for dr, dc in d:
                rn, cn = r + dr, c + dc
                if rn < 0 or rn == rows or cn < 0 or cn == cols:
                    continue
                if matrix[r][c] >= matrix[rn][cn] and not reversed:
                    continue
                if matrix[r][c] <= matrix[rn][cn] and reversed:
                    continue
                res.append(cols * rn + cn)
            return res

        def dfs(i, current):
            nonlocal rows, cols
            if dag[i] == 2:
                return
            dag[i] = 1
            current.append(i)
            for nxt in siblings(i):
                dfs(nxt, current)
            current.pop()
            dag[i] = 2
            t_sorted.append(i)

        for i in range(len(dag)):
            dfs(i, [])
        t_sorted.reverse()

        print(t_sorted)

        dag = [1] * (rows * cols)
        for i in t_sorted:
            for s in siblings(i, True):
                dag[i] = max(dag[i], dag[s] + 1)
        return max(dag)


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]

t = Solution()
checkValue(4, t.longestIncreasingPath(matrix))