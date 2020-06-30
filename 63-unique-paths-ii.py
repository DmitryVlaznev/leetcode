# 63. Unique Paths II

# A robot is located at the top-left corner of a m x n grid (marked
# 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The
# robot is trying to reach the bottom-right corner of the grid (marked
# 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique
# paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the
# grid.

# Note: m and n will be at most 100.

# Example 1:
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2

# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0] * (m + 1) for i in range(n + 1)]
        dp[1][0] = 1

        dp[1][0] = 1
        for c in range(1, m + 1):
            for r in range(1, n + 1):
                if obstacleGrid[r - 1][c - 1] == 1: continue
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[n][m]


def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
log(2, t.uniquePathsWithObstacles(grid))

grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
log(6, t.uniquePathsWithObstacles(grid))

grid = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
log(4, t.uniquePathsWithObstacles(grid))

grid = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
log(0, t.uniquePathsWithObstacles(grid))
