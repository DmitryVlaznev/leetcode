# 221. Maximal Square

# Given a 2D binary matrix filled with 0's and 1's, find the largest
# square containing only 1's and return its area.

# Example:
# Input:
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Output: 4

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if rows == 0: return 0
        cols = len(matrix[0])
        if cols == 0: return 0
        max_square = 0
        dp = [[0] * (cols + 1) for i in range(rows + 1)]

        for i in range(rows):
            p = i + 1
            for j in range(cols):
                q = j + 1
                if matrix[i][j] == "0":
                    dp[p][q] = 0
                    continue
                dp[p][q] = min(dp[p - 1][q - 1], dp[p - 1][q], dp[p][q - 1]) + 1
                max_square = max(max_square, dp[p][q])
        return max_square ** 2


t = Solution()
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print("4 = ", t.maximalSquare(matrix))

matrix = [
    ["0", "0", "0", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["0", "1", "1", "1", "1"],
    ["0", "1", "1", "1", "1"],
]
print("16 = ", t.maximalSquare(matrix))

matrix = [
    ["1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1"],
    ["0", "1", "1", "1", "1", "1"],
    ["0", "1", "1", "1", "1", "1"],
]
print("16 = ", t.maximalSquare(matrix))

matrix = [["1"]]
print("1 = ", t.maximalSquare(matrix))

matrix = [["0"]]
print("0 = ", t.maximalSquare(matrix))

matrix = [
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
print("0 = ", t.maximalSquare(matrix))

matrix = [
    ["1", "0", "1", "0", "1"],
    ["0", "1", "0", "1", "1"],
    ["1", "0", "1", "0", "1"],
    ["0", "1", "0", "1", "0"],
]
print("1 = ", t.maximalSquare(matrix))

matrix = [
    ["1", "0", "1", "1", "0"],
]
print("1 = ", t.maximalSquare(matrix))

matrix = [
    ["1"], ["0"], ["1"], ["1"], ["0"],
]
print("1 = ", t.maximalSquare(matrix))

matrix = [[]]
print("0 = ", t.maximalSquare(matrix))

matrix = []
print("0 = ", t.maximalSquare(matrix))