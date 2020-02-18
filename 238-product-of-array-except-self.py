# 238. Product of Array Except Self

# Given an array nums of n integers where n > 1,  return an array output
# such that output[i] is equal to the product of all the elements of
# nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array
# does not count as extra space for the purpose of space complexity
# analysis.)

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l

        # Put left products to a res array.
        left = nums[0]
        for i in range(1, l):
            res[i] = res[i - 1] * left
            left = nums[i]

        # Calculate right products and res simultaneously.
        product = 1
        for i in range(l - 2, -1, -1):
            res[i] = res[i] * nums[i + 1] * product
            product = product * nums[i + 1]

        return res


test = Solution()
print("[24, 12, 8, 6] = ", test.productExceptSelf([1,2,3,4]))
print("[6, 5, 30] = ", test.productExceptSelf([5, 6, 1]))
print("[3, 4] = ", test.productExceptSelf([4,3]))