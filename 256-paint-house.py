# 256. Paint House

# Medium

# There is a row of n houses, where each house can be painted one of
# three colors: red, blue, or green. The cost of painting each house
# with a certain color is different. You have to paint all the houses
# such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by
# an n x 3 cost matrix costs.

# For example, costs[0][0] is the cost of painting house 0 with the
# color red; costs[1][2] is the cost of painting house 1 with color
# green, and so on...

# Return the minimum cost to paint all houses.

# Example 1:
# Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint
# house 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10.

# Example 2:
# Input: costs = [[7,6,2]]
# Output: 2

# Constraints:
# costs.length == n
# costs[i].length == 3
# 1 <= n <= 100
# 1 <= costs[i][j] <= 20

from typing import List
from functools import lru_cache


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0] * 3 for _ in range(n + 1)]
        for i in range(1, n + 1):
            cc = costs[i - 1]
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cc[0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cc[1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cc[2]
        return min(dp[-1])

    def minCost2(self, costs: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def dp(i, prev_color):
            if i == len(costs):
                return 0
            res = float("inf")
            for c in range(0, 3):
                if c == prev_color:
                    continue
                res = min(res, costs[i][c] + dp(i + 1, c))
            return res

        return dp(0, -1)
