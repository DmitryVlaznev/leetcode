# 931. Minimum Falling Path Sum

# Given an n x n array of integers matrix, return the minimum sum of any
# falling path through matrix.

# A falling path starts at any element in the first row and chooses the
# element in the next row that is either directly below or diagonally
# left/right. Specifically, the next element from position (row, col)
# will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

# Example 1:
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.

# Example 2:
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.

# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0][:]
        for row in range(1, n):
            dp_row = [0] * n
            for col in range(0, n):
                left = dp[col - 1] if col > 0 else float("inf")
                top = dp[col]
                right = dp[col + 1] if col < n - 1 else float("inf")
                dp_row[col] = min(left, top, right) + matrix[row][col]
            dp = dp_row
        return min(dp)

    def minFallingPathSum2(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float("inf")] * n for _ in range(n)]
        dp[0] = matrix[0][:]

        for row in range(1, n):
            for col in range(0, n):
                left = dp[row - 1][col - 1] if col > 0 else float("inf")
                top = dp[row - 1][col]
                right = dp[row - 1][col + 1] if col < n - 1 else float("inf")
                dp[row][col] = min(left, top, right) + matrix[row][col]
        return min(dp[-1])


s = Solution()
s.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]])
