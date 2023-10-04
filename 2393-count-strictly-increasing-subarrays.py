# 2393. Count Strictly Increasing Subarrays

# Medium

# You are given an array nums consisting of positive integers.

# Return the number of subarrays of nums that are in strictly increasing
# order.

# A subarray is a contiguous part of an array.


# Example 1:
# Input: nums = [1,3,5,4,4,6]
# Output: 10
# Explanation: The strictly increasing subarrays are the following:
# - Subarrays of length 1: [1], [3], [5], [4], [4], [6].
# - Subarrays of length 2: [1,3], [3,5], [4,6].
# - Subarrays of length 3: [1,3,5].
# The total number of subarrays is 6 + 3 + 1 = 10.

# Example 2:
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: Every subarray is strictly increasing. There are 15
# possible subarrays that we can take.


# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        start, res = 0, 0
        for i in range(1, len(nums)):
            res += i - start
            if nums[i] <= nums[i - 1]:
                start = i
        res += len(nums) - start
        return res


from utils import checkValue

s = Solution()
checkValue(10, s.countSubarrays([1, 3, 5, 4, 4, 6]))
checkValue(15, s.countSubarrays([1, 2, 3, 4, 5]))
checkValue(5, s.countSubarrays([1, 1, 1, 1, 1]))
checkValue(1, s.countSubarrays([1]))
