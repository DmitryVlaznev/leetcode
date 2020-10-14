# 213. House Robber II

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed. All houses at this
# place are arranged in a circle. That means the first house is the
# neighbor of the last one. Meanwhile, adjacent houses have a security
# system connected, and it will automatically contact the police if two
# adjacent houses were broken into on the same night.

# Given a list of non-negative integers nums representing the amount of
# money of each house, return the maximum amount of money you can rob
# tonight without alerting the police.

# Example 1:
# Input: nums = [2,3,2]
# Output: 3

# Explanation: You cannot rob house 1 (money = 2) and then rob house 3
# (money = 2), because they are adjacent houses.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 3:
# Input: nums = [0]
# Output: 0


# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

from typing import List
from utils import checkValue

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0 if not nums else nums[0]

        second_last = last = 0
        for n in nums[0:-1]: second_last, last = last, max(second_last + n, last)
        v0 = last
        second_last = last = 0
        for n in nums[1:]: second_last, last = last, max(second_last + n, last)
        v1 = last
        return max(v0, v1)

t = Solution()
checkValue(3, t.rob([2,3,2]))
checkValue(4, t.rob([1,2,3,1]))
checkValue(0, t.rob([0]))
checkValue(0, t.rob([]))
checkValue(16, t.rob([8,9,8,1]))
checkValue(1, t.rob([1]))
checkValue(3, t.rob([2,3]))
checkValue(3, t.rob([3,2]))