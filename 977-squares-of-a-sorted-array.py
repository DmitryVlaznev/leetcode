# 977. Squares of a Sorted Array

# Easy

# Given an integer array nums sorted in non-decreasing order, return an
# array of the squares of each number sorted in non-decreasing order.


# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

from typing import List
from utils import checkList


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p = 0
        while p < len(nums) and nums[p] < 0:
            p += 1
        q, res = p - 1, []
        while q >= 0 or p < len(nums):
            left = nums[q] ** 2 if q >= 0 else float("inf")
            right = nums[p] ** 2 if p < len(nums) else float("inf")
            if left <= right:
                res.append(left)
                q -= 1
            else:
                res.append(right)
                p += 1
        return res


t = Solution()
checkList([0, 1, 9, 16, 100], t.sortedSquares([-4, -1, 0, 3, 10]))
checkList([4, 9, 9, 49, 121], t.sortedSquares([-7, -3, 2, 3, 11]))
checkList([1], t.sortedSquares([-1]))
checkList([1], t.sortedSquares([1]))
checkList([1, 9], t.sortedSquares([-3, -1]))
checkList([1, 9], t.sortedSquares([1, 3]))
