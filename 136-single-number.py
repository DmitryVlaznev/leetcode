# 136. Single Number

# Given a non-empty array of integers, every element appears twice
# except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you
# implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i == 0:
                res = num
                continue

            res = res ^ num

        return res

test = Solution()
print("1 = ", test.singleNumber([2,2,1]))
print("4 = ", test.singleNumber([4,1,2,1,2]))


