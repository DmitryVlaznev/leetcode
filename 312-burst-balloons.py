# 312. Burst Balloons

# Hard

# Given n balloons, indexed from 0 to n-1. Each balloon is painted with
# a number on it represented by array nums. You are asked to burst all
# the balloons. If the you burst balloon i you will get nums[left] *
# nums[i] * nums[right] coins. Here left and right are adjacent indices
# of i. After the burst, the left and right then becomes adjacent.

# Find the maximum coins you can collect by bursting the balloons
# wisely.

# Note:
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore
# you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

# Example:
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

from typing import List
from utils import checkValue


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        dp = [[0] * n for _ in nums]

        for length in range(1, n + 1):
            for start in range(0, n - length + 1):
                end = start + length - 1
                for k in range(start, end + 1):
                    left = 1 if start == 0 else nums[start - 1]
                    right = 1 if end == n - 1 else nums[end + 1]
                    before = 0 if k == start else dp[start][k - 1]
                    after = 0 if k == end else dp[k + 1][end]
                    dp[start][end] = max(
                        left * nums[k] * right + before + after, dp[start][end]
                    )
        return dp[0][-1]


t = Solution()
checkValue(167, t.maxCoins([3, 1, 5, 8]))
checkValue(36, t.maxCoins([2, 1, 5, 2]))
checkValue(0, t.maxCoins([]))
checkValue(13, t.maxCoins([13]))
