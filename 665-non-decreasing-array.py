# 665. Non-decreasing Array

# Medium

# Given an array nums with n integers, your task is to check if it could
# become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds
# for every i (0-based) such that (0 <= i <= n - 2).

# Example 1:
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.

# Example 2:
# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most
# one element.

# Constraints:
# n == nums.length
# 1 <= n <= 104
# -10^5 <= nums[i] <= 10^5

from typing import List
from utils import checkValue


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        skipped, last = False, 0
        for i in range(1, len(nums)):
            n = nums[i]
            if n >= nums[last]:
                last = i
                continue
            if skipped:
                return False
            skipped = True
            if last == 0 or n >= nums[last - 1]:
                last = i
        return True


t = Solution()

checkValue(False, t.checkPossibility([3, 4, 2, 3]))
checkValue(True, t.checkPossibility([4, 2, 3]))
checkValue(False, t.checkPossibility([4, 2, 1]))
checkValue(False, t.checkPossibility([1, 4, 2, 3, 4, 3, 4]))
checkValue(True, t.checkPossibility([2, 4, 2, 3, 4]))
checkValue(True, t.checkPossibility([5, 7, 1, 8]))
