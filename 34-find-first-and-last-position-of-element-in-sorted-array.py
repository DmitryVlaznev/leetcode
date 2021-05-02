# Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the
# starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# Follow up: Could you write an algorithm with O(log n) runtime
# complexity?


# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]

# Constraints:
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9

from typing import List
from utils import checkList


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = -1, len(nums)
        while r - l > 1:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        if r == len(nums) or nums[r] != target:
            return [-1, -1]
        left = r

        l, r = -1, len(nums)
        while r - l > 1:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        return [left, l]


t = Solution()

checkList([3, 4], t.searchRange([5, 7, 7, 8, 8, 10], 8))
checkList([0, 0], t.searchRange([5, 7, 7, 8, 8, 10], 5))
checkList([1, 1], t.searchRange([5, 6, 7, 7, 8, 8, 10], 6))
checkList([5, 5], t.searchRange([5, 7, 7, 8, 8, 10], 10))
checkList([-1, -1], t.searchRange([5, 7, 7, 8, 8, 10], 6))
checkList([0, 0], t.searchRange([10], 10))
checkList([-1, -1], t.searchRange([], 6))
checkList([-1, -1], t.searchRange([4], 6))
