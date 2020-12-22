# 334. Increasing Triplet Subsequence

# Medium

# Given an integer array nums, return true if there exists a triple of
# indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
# If no such indices exists, return false.

# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.

# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 <
# nums[4] == 4 < nums[5] == 6.

# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1

# Follow up: Could you implement a solution that runs in O(n) time
# complexity and O(1) space complexity?

from typing import List
from utils import checkValue


class Solution:
    # O(n)
    def increasingTriplet(self, nums: List[int]) -> bool:

        first_min = second_min = float("inf")
        for n in nums:
            if n > first_min and n > second_min:
                return True
            if n <= first_min:
                first_min = n
            elif n <= second_min:
                second_min = n
        return False

    # O(n^2)
    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     dp = [0] * len(nums)

    #     for i, n in enumerate(nums):
    #         for j in range(0, i):
    #             if nums[j] < n:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #             if dp[i] >= 2:
    #                 return True
    #     return False


t = Solution()

checkValue(True, t.increasingTriplet([1, 2, 3, 4, 5]))
checkValue(False, t.increasingTriplet([5, 4, 3, 2, 1]))
checkValue(True, t.increasingTriplet([1, 2, 3, 4, 5]))
checkValue(True, t.increasingTriplet([1, 2, 1, 1, 5]))
checkValue(False, t.increasingTriplet([1, 2]))
checkValue(False, t.increasingTriplet([1, 0, 0, 1]))
checkValue(True, t.increasingTriplet([1, 0, 0, 0, 2, 0, 0, -1, -1, -1, -1, 3]))
