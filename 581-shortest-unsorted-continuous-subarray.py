# 581. Shortest Unsorted Continuous Subarray

# Given an integer array, you need to find one continuous subarray that
# if you only sort this subarray in ascending order, then the whole
# array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5

# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to
# make the whole array sorted in ascending order.

# Note:
# * Then length of the input array is in range [1, 10,000].
# * The input array may contain duplicates, so ascending order here
#   means <=.

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0

        left = 1
        while left < len(nums) and nums[left] >= nums[left - 1]:
            left += 1
        if left == len(nums): return 0

        right = len(nums) - 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1


        vmin = nums[left]
        for i in range(min(left, right), max(left, right) + 1):
            vmin = vmin if nums[i] > vmin else nums[i]
        while left > 0 and vmin < nums[left - 1]:
            left -= 1

        vmax = nums[left]
        for i in range(min(left, right), max(left, right) + 1):
            vmax = vmax if nums[i] < vmax else nums[i]
        while right < len(nums) - 1 and vmax > nums[right + 1]:
            right += 1

        return right - left + 1

        # print("left", left, "right", right, "min", vmin, "max", vmax)
        # print("left", left, "right", right)

test = Solution()

print("5 >> ", test.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print("2 >> ", test.findUnsortedSubarray([2, 4, 10, 8, 15]))
print("3 >> ", test.findUnsortedSubarray([1, 2, 4, 5, 3]))
print("2 >> ", test.findUnsortedSubarray([3, 2, 4, 5, 6]))
print("4 >> ", test.findUnsortedSubarray([1, 1, 1, 1, 1, 5, 5, 4, 4, 7, 7, 7, 7]))
print("4 >> ", test.findUnsortedSubarray([1, 1, 5, 5, 4, 4, 7, 7]))
print("8 >> ", test.findUnsortedSubarray([3, 2, 0, 0, 0, 0, 5, 4]))
print("0 >> ", test.findUnsortedSubarray([2, 4, 8, 10, 15]))
print("0 >> ", test.findUnsortedSubarray([2, 4]))
print("2 >> ", test.findUnsortedSubarray([5, 4]))
print("0 >> ", test.findUnsortedSubarray([5, 5, 5]))
print("4 >> ", test.findUnsortedSubarray([1, 3, 5, 4, 2]))
print("4 >> ", test.findUnsortedSubarray([1, 3, 2, 2, 2]))