# 53. Maximum Subarray

# Given an integer array nums, find the contiguous
# subarray (containing at least one number) which has the largest sum
# and return its sum.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution
# using the divide and conquer approach, which is more subtle.

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = max_sum = float("-inf")
        for i in nums:
            if sum < 0:
                sum = i
            else:
                sum += i
            max_sum = max(sum, max_sum)
        return max_sum

test = Solution()

print("6 >> ", test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print("-1 >> ", test.maxSubArray([-2,-3,-1,-5]))
print("6 >> ", test.maxSubArray([2,3,1,0]))
print("2 >> ", test.maxSubArray([2,-2,2,-2]))