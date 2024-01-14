# 487. Max Consecutive Ones II

# Medium

# Given a binary array nums, return the maximum number of consecutive
# 1's in the array if you can flip at most one 0.

# Example 1:
# Input: nums = [1,0,1,1,0]
# Output: 4
# Explanation:
# - If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
# - If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
# The max number of consecutive ones is 4.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 4
# Explanation:
# - If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
# - If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
# The max number of consecutive ones is 4.


# Constraints:
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.


# Follow up: What if the input numbers come in one by one as an infinite
# stream? In other words, you can't store all numbers coming from the
# stream as it's too large to hold in memory. Could you solve it
# efficiently?

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_start, next_start, have_zero, res = 0, -1, nums[0] == 0, 1

        for i in range(1, len(nums)):
            if nums[i] == 1:
                if nums[i - 1] == 0:
                    next_start = i
            else:
                if have_zero:
                    current_start = next_start if next_start > -1 else i
                    next_start = -1
                else:
                    have_zero = True
            res = max(res, i - current_start + 1)
        return res

    def findMaxConsecutiveOnes2(nums):
        max_ones = 0  # To store the maximum consecutive ones
        left = 0  # Left pointer of the sliding window
        flips_used = 0  # Number of flips used

        for right in range(len(nums)):
            if nums[right] == 0:
                flips_used += 1

                while flips_used > 2:
                    if nums[left] == 0:
                        flips_used -= 1
                    left += 1

            # Update the maximum consecutive ones
            max_ones = max(max_ones, right - left + 1)

        return max_ones


from utils import checkValue

s = Solution()
# checkValue(4, s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
# checkValue(4, s.findMaxConsecutiveOnes([0, 0, 1, 1, 0, 1]))
# checkValue(4, s.findMaxConsecutiveOnes([1, 1, 1, 1]))
# checkValue(1, s.findMaxConsecutiveOnes([0, 0, 0]))
# checkValue(4, s.findMaxConsecutiveOnes([1, 0, 1, 1, 0]))
# checkValue(2, s.findMaxConsecutiveOnes([1, 0]))
# checkValue(2, s.findMaxConsecutiveOnes([0, 1]))
# checkValue(4, s.findMaxConsecutiveOnes([0, 1, 0, 1, 1, 0, 1]))
# checkValue(4, s.findMaxConsecutiveOnes([0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1]))


checkValue(6, s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
checkValue(2, s.findMaxConsecutiveOnes([0, 0]))
checkValue(3, s.findMaxConsecutiveOnes([1, 0, 1]))
checkValue(4, s.findMaxConsecutiveOnes([1, 0, 1, 0, 0, 1]))
checkValue(3, s.findMaxConsecutiveOnes([1, 0, 0, 0, 1, 0, 0, 0, 0, 1]))
