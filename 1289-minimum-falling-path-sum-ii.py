# 1289. Minimum Falling Path Sum II

# Hard

# Given an n x n integer matrix grid, return the minimum sum of a
# falling path with non-zero shifts.

# A falling path with non-zero shifts is a choice of exactly one element
# from each row of grid such that no two elements chosen in adjacent
# rows are in the same column.

# Example 1:
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 13
# Explanation:
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.

# Example 2:
# Input: grid = [[7]]
# Output: 7


# Constraints:
# n == grid.length == grid[i].length
# 1 <= n <= 200
# -99 <= grid[i][j] <= 99

from typing import List


class Solution:
    # O(n^2)
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        dp[0] = grid[0][:]

        for row in range(n - 1):
            m1 = m2 = float("inf")
            for col in range(n):
                if dp[row][col] < m1:
                    m2, m1 = m1, dp[row][col]
                elif dp[row][col] < m2:
                    m2 = dp[row][col]

            for col in range(n):
                min_row_value = m1 if dp[row][col] != m1 else m2
                dp[row + 1][col] = min_row_value + grid[row + 1][col]

        return min(dp[-1])

    # O(n^3)
    def minFallingPathSum2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        dp[0] = grid[0][:]

        for row in range(n - 1):
            for col in range(n):
                min_row_value = float("inf")
                for i in range(n):
                    if i != col:
                        min_row_value = min(min_row_value, dp[row][i])
                dp[row + 1][col] = min_row_value + grid[row + 1][col]
        return min(dp[-1])


s = Solution()
s.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
