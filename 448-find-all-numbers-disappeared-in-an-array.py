# 448. Find All Numbers Disappeared in an Array

# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
# some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this
# array.

# Could you do it without extra space and in O(n) runtime? You may
# assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            i = abs(num) - 1
            if nums[i] < 0:
                continue
            nums[i] = -1 * nums[i]

        disappeared = []

        for i in range(len(nums)):
            if nums[i] > 0:
                disappeared.append(i + 1)

        return disappeared

test = Solution()
print("[5, 6] = ", test.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print("[2] = ", test.findDisappearedNumbers([1,1,3]))
