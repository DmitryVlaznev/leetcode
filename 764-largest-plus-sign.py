# 764. Largest Plus Sign

# Medium

# You are given an integer n. You have an n x n binary grid grid with
# all values initially 1's except for some indices given in the array
# mines. The ith element of the array mines is defined as mines[i] =
# [xi, yi] where grid[xi][yi] == 0.

# Return the order of the largest axis-aligned plus sign of 1's
# contained in grid. If there is none, return 0.

# An axis-aligned plus sign of 1's of order k has some center grid[r][c]
# == 1 along with four arms of length k - 1 going up, down, left, and
# right, and made of 1's. Note that there could be 0's or 1's beyond the
# arms of the plus sign, only the relevant area of the plus sign is
# checked for 1's.

# Example 1:
# Input: n = 5, mines = [[4,2]]
# Output: 2
# Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.

# Example 2:
# Input: n = 1, mines = [[0,0]]
# Output: 0
# Explanation: There is no plus sign, so return 0.

# Constraints:
# 1 <= n <= 500
# 1 <= mines.length <= 5000
# 0 <= xi, yi < n
# All the pairs (xi, yi) are unique.

from typing import List
from utils import checkValue


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        v = lambda: {"t": 0, "r": 0, "b": 0, "l": 0}
        dp = [[v() for __ in range(n)] for _ in range(n)]

        for r, c in mines:
            dp[r][c] = None

        for r in range(n):
            for c in range(n):
                if dp[r][c] == None:
                    continue
                dp[r][c]["l"] = (
                    dp[r][c - 1]["l"] + 1 if c > 0 and dp[r][c - 1] is not None else 0
                )
                dp[r][c]["t"] = (
                    dp[r - 1][c]["t"] + 1 if r > 0 and dp[r - 1][c] is not None else 0
                )
        for r in reversed(range(n)):
            for c in reversed(range(n)):
                if dp[r][c] == None:
                    continue
                dp[r][c]["r"] = (
                    dp[r][c + 1]["r"] + 1
                    if c < n - 1 and dp[r][c + 1] is not None
                    else 0
                )
                dp[r][c]["b"] = (
                    dp[r + 1][c]["b"] + 1
                    if r < n - 1 and dp[r + 1][c] is not None
                    else 0
                )

        res = 0
        for r in range(n):
            for c in range(n):
                if dp[r][c] == None:
                    continue
                res = max(
                    res,
                    min(dp[r][c]["t"], dp[r][c]["r"], dp[r][c]["b"], dp[r][c]["l"]) + 1,
                )
        return res


s = Solution()
checkValue(2, s.orderOfLargestPlusSign(5, [[4, 2]]))
checkValue(0, s.orderOfLargestPlusSign(1, [[0, 0]]))
checkValue(1, s.orderOfLargestPlusSign(2, [[0, 0], [1, 1]]))