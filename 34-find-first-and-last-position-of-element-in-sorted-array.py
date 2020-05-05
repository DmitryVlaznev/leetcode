# 34. Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums_length = len(nums)
        res = [-1, -1]
        if not nums_length: return res
        l = -1
        r = nums_length
        while r - l > 1:
            mid = l + (r - l) // 2
            if nums[mid] < target: l = mid
            else: r = mid
        if r > nums_length - 1 or nums[r] != target: return res

        res[0] = r
        l = -1
        r = nums_length
        while r - l > 1:
            mid = l + (r - l) // 2
            if nums[mid] <= target: l = mid
            else: r = mid
        res[1] = l
        return res

t = Solution()
print("[3, 4] = ", t.searchRange([5,7,7,8,8,10], 8))
print("[5, 5] = ", t.searchRange([5,7,7,8,8,10], 10))
print("[-1,-1] = ", t.searchRange([5,7,7,8,8,10], 6))
print("[-1,-1] = ", t.searchRange([5,7,7,8,8,10], 3))
print("[-1,-1] = ", t.searchRange([5,7,7,8,8,10], 42))
print("[-1,-1] = ", t.searchRange([], 42))
print("[0,0] = ", t.searchRange([5,7,7,8,8,10], 5))
print("[0,0] = ", t.searchRange([1, 2], 1))
print("[0,0] = ", t.searchRange([1], 1))
print("[1,1] = ", t.searchRange([1, 2], 2))