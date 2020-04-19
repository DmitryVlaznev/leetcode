# 33. Search in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated at some pivot
# unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return
# its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

from typing import List


class Solution:
    def get_pivot(self, nums, l):
        if nums[0] < nums[l - 1]: return 0
        s = 0
        e = l - 1
        while s <= e:
            p = (e - s) // 2 + s
            left = nums[p - 1] if p > 0 else float("inf")
            right = nums[p + 1] if p < l - 1 else float("inf")
            if nums[p] < left and nums[p] < right:
                return p
            if nums[p] >= nums[e]: s = p + 1
            if nums[p] <= nums[e]: e = p - 1
        return p

    def search(self, nums: List[int], target: int) -> int:

        l = len(nums)
        if l == 0: return -1
        if l == 1: return 0 if nums[0] == target else -1

        pivot = self.get_pivot(nums, l)
        s = 0
        e = l - 1
        while s <= e:
            p = (e - s) // 2 + s
            pi = (pivot + p) % l
            if nums[pi] == target: return pi
            if nums[pi] > target: e = p - 1
            else: s = p + 1
        return -1

t = Solution()
print(" 4 = ", t.search([4,5,6,7,0,1,2], 0))
print(" 5 = ", t.search([4,5,6,7,0,1,2], 1))
print(" 0 = ", t.search([4,5,6,7,0,1,2], 4))
print(" 2 = ", t.search([42,43,16,17], 16))
print(" 3 = ", t.search([42,43,16,17], 17))
print("-1 = ", t.search([4,5,6,7,0,1,2], 3))
print("-1 = ", t.search([0,1,2,4,5,6,7], 17))
print("-1 = ", t.search([], 5))
print("-1 = ", t.search([3,1], 0))
print(" 0 = ", t.search([3,1], 3))
print(" 1 = ", t.search([3,1], 1))
print("-1 = ", t.search([2,3,1], 0))
print(" 1 = ", t.search([2,3,1], 3))

# print("s = ", s, "e = ", e, "p = ", p)

