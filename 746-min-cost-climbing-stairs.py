# 746. Min Cost Climbing Stairs

# Easy

# You are given an integer array cost where cost[i] is the cost of ith
# step on a staircase. Once you pay the cost, you can either climb one
# or two steps.

# You can either start from the step with index 0, or the step with
# index 1.

# Return the minimum cost to reach the top of the floor.

# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: Cheapest is: start on cost[1], pay that cost, and go to
# the top.

# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: Cheapest is: start on cost[0], and only step on 1s,
# skipping cost[3].

# Constraints:
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

from typing import List
from functools import lru_cache


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l, r = cost[0], cost[1]
        for c in cost[2:]:
            t = min(l + c, r + c)
            l, r = r, t
        return min(l, r)

    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        @lru_cache(maxsize=None)
        def step(i):
            if i >= len(cost):
                return 0

            return cost[i] + min(step(i + 1), step(i + 2))

        return min(step(0), step(1))
