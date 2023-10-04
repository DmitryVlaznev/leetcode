# 896. Monotonic Array

# Easy

# An array is monotonic if it is either monotone increasing or monotone
# decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <=
# nums[j]. An array nums is monotone decreasing if for all i <= j,
# nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is
# monotonic, or false otherwise.


# Example 1:
# Input: nums = [1,2,2,3]
# Output: true

# Example 2:
# Input: nums = [6,5,4,4]
# Output: true

# Example 3:
# Input: nums = [1,3,2]
# Output: false


# Constraints:
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True

        d = lambda a, b: 0 if a == b else -1 if a < b else 1
        res = 0
        for i in range(1, len(nums)):
            di = d(nums[i], nums[i - 1])
            if di == 0:
                continue
            if res == 0:
                res = di
            if res != di:
                return False
        return True
