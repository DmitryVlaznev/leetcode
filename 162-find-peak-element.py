# 162. Find Peak Element

# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak
# element and return its index.

# The array may contain multiple peaks, in that case return the index to
# any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the
#              index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the
#              peak element is 2, or index number 5 where the peak
#              element is 6.

# Note:
# Your solution should be in logarithmic complexity.

from typing import List


class Solution:
    def findRecursively(self, nums: List[int], start: int, end: int) -> int:
        if start == end:
            return start

        mid = start + (end - start) // 2
        if mid == 0 and nums[0] > nums[1]: return 0
        if mid == len(nums) - 1 and nums[mid] > nums[mid - 1]: return mid
        if mid in range(1, (len(nums) - 1)) and nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]: return mid

        if nums[mid + 1] > nums[mid]: return self.findRecursively(nums, mid + 1, end)
        return self.findRecursively(nums, start, mid - 1)


    def findPeakElement(self, nums: List[int]) -> int:
        return self.findRecursively(nums, 0, len(nums) - 1)


test = Solution()

print("2 >> ", test.findPeakElement([1,2,3,1]))
print("1 | 5 >> ", test.findPeakElement([1,2,1,3,5,6,4]))
print("3 >> ", test.findPeakElement([1,2,3,4]))
print("0 >> ", test.findPeakElement([5,4,3,2,1]))
print("1 | 3 >> ", test.findPeakElement([1,2,1,2,1]))