# 594. Longest Harmonious Subsequence

# Easy

# We define a harmonious array as an array where the difference between
# its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest
# harmonious subsequence among all its possible subsequences.

# A subsequence of array is a sequence that can be derived from the
# array by deleting some or no elements without changing the order of
# the remaining elements.

# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 2

# Example 3:
# Input: nums = [1,1,1,1]
# Output: 0

# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -10^9 <= nums[i] <= 10^9

from typing import List
from utils import checkValue


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        seen = {}
        res = 0
        for n in nums:
            if n not in seen:
                seen[n] = 0
            seen[n] += 1
            less = seen[n - 1] if n - 1 in seen else 0
            greater = seen[n + 1] if n + 1 in seen else 0
            if less == greater == 0:
                continue
            res = max(res, max(less, greater) + seen[n])
        return res


t = Solution()
checkValue(5, t.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
checkValue(2, t.findLHS([1, 2, 3, 4]))
checkValue(0, t.findLHS([1, 1, 1, 1]))
