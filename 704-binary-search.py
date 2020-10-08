# 704. Binary Search

# Given a sorted (in ascending order) integer array nums of n elements
# and a target value, write a function to search target in nums. If
# target exists, then return its index, otherwise return -1.


# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Note:
# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].

from typing import List
from utils import checkValue

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        l = -1
        r = len(nums)
        while r - l > 1:
            m = l + (r - l) // 2
            if nums[m] == target: return m
            if nums[m] > target: r = m
            else: l = m
        return -1

t = Solution()
checkValue(4, t.search([-1,0,3,5,9,12], 9))
checkValue(5, t.search([-1,0,3,5,9,12], 12))
checkValue(0, t.search([-1,0,3,5,9,12], -1))
checkValue(-1, t.search([-1,0,3,5,9,12], 2))
checkValue(-1, t.search([3], 2))
checkValue(0, t.search([3], 3))
checkValue(-1, t.search([], 3))
checkValue(1, t.search([2,3], 3))
checkValue(0, t.search([2,3], 2))
checkValue(-1, t.search([2,3], 1))
checkValue(-1, t.search([2,3], 15))

