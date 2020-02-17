# 268. Missing Number

# Given an array containing n distinct numbers taken from 0, 1, 2, ...,
# n, find the one that is missing from the array.

# Example 1:
# Input: [3,0,1]
# Output: 2

# Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

# Note:
# Your algorithm should run in linear runtime complexity. Could you
# implement it using only constant extra space complexity?

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        sequenceSum = (n - 1) * n / 2;
        sum = 0
        for num in nums:
            sum = sum + num
        return int(sequenceSum - sum)

test = Solution()
print("2 = ", test.missingNumber([3,0,1]))
print("8 = ", test.missingNumber([9,6,4,2,3,5,7,0,1]))
print("0 = ", test.missingNumber([2,1,3]))
print("0 = ", test.missingNumber([1]))
print("1 = ", test.missingNumber([0]))