# 154. Find Minimum in Rotated Sorted Array II

# Suppose an array sorted in ascending order is rotated at some pivot
# unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.

# Example 1:

# Input: [1,3,5]
# Output: 1
# Example 2:

# Input: [2,2,2,0,1]
# Output: 0
# Note:

# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?

from typing import List


class Solution:
    def findSubMin(self, nums: List[int], l, r) -> int:
        if r - l < 2: return min(nums[l], nums[r])
        mid = l + (r - l)//2

        if nums[mid] == nums[l] and nums[mid] == nums[r]:
            return min(self.findSubMin(nums, l, mid), self.findSubMin(nums, mid, r))
        if nums[mid] >= nums[l]: return self.findSubMin(nums, mid, r)
        elif nums[mid] < nums[l]: return self.findSubMin(nums, l, mid)

    def findMin(self, nums: List[int]) -> int:
        last_idx = len(nums) - 1
        if nums[0] < nums[last_idx]: return nums[0]
        return self.findSubMin(nums, 0, last_idx)

# l = len(nums)
# if l == 1: re
# l = -1
# r = len(nums)
# first = nums[0]
# last = nums[r - 1]
# if first <= last: return first
# while r - l > 1:
#     mid = l + (r - l)//2
#     if nums[mid] > first: l = mid
#     else: r = mid
# return nums[r] if r < len(nums) else nums[l]

# print("----------")
# print("l = ", l, "nums[l] = ", nums[l], "r = ", r, "nums[r] = ", nums[r])
# print("mid = ", mid, "nums[mid] = ", nums[mid])

t = Solution()
print("0 = ", t.findMin([4,5,6,7,0,1,2]))
print("1 = ", t.findMin([1,3,5]))
print("1 = ", t.findMin([1,1,1]))
print("0 = ", t.findMin([2,2,2,0,1]))
print("0 = ", t.findMin([2,2,0,2,2,2,2,2,2]))
print("0 = ", t.findMin([2,0,2,2]))
print("0 = ", t.findMin([0,2,2]))