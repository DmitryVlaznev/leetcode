# 153. Find Minimum in Rotated Sorted Array

# Suppose an array sorted in ascending order is rotated at some pivot unknown to
# you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:
# Input: [3,4,5,1,2]
# Output: 1

# Example 2:
# Input: [4,5,6,7,0,1,2]
# Output: 0

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l = -1
        # r = len(nums)
        # while r - l > 1:
        #     mid = l + (r - l) // 2
        #     right = nums[r] if r < len(nums) else nums[-1]
        #     if nums[mid] > right: l = mid
        #     else: r = mid
        # return nums[r]

        l = -1
        r = len(nums) - 1
        while r - l > 1:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]: l = mid
            else: r = mid
        return nums[r]

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(1, t.findMin([3,4,5,1,2]))
log(0, t.findMin([4,5,6,7,0,1,2]))
log(1, t.findMin([6,7,1,2,3,4,5]))
log(1, t.findMin([3,4,5,6,7,1,2]))
log(1, t.findMin([5,6,7,1,2,3,4]))
log(1, t.findMin([1,2,3,4,5,6,7]))
log(1, t.findMin([2,3,4,5,6,7,1]))
log(2, t.findMin([2,3]))
log(2, t.findMin([3,2]))
log(2, t.findMin([2]))