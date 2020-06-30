# 62. Unique Paths

# A robot is located at the top-left corner of a m x n grid (marked
# 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The
# robot is trying to reach the bottom-right corner of the grid (marked
# 'Finish' in the diagram below).

# How many possible unique paths are there?

# Example 1:
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

# Example 2:
# Input: m = 7, n = 3
# Output: 28

# Constraints:
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # O(m*n) space complexity
        # dp = [[0] * (m + 1) for i in range(n + 1)]
        # dp[1][0] = 1
        # for c in range(1, m + 1):
        #     for r in range(1, n + 1):
        #         dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        # print(dp)
        # return dp[n][m]

        # O(m) space complexity
        dp = [0] * (m + 1)
        dp[1] = 1
        for r in range(0, n):
            for c in range(1, m + 1):
                dp[c] = max(dp[c] + dp[c - 1], 1)
        return dp[-1]

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log(3, t.uniquePaths(3, 2))
log(10, t.uniquePaths(4, 3))
log(28, t.uniquePaths(7, 3))
log(1, t.uniquePaths(7, 1))
log(1, t.uniquePaths(1, 3))