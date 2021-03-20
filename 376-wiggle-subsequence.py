# 376. Wiggle Subsequence

# Medium

# Given an integer array nums, return the length of the longest wiggle
# sequence.

# A wiggle sequence is a sequence where the differences between
# successive numbers strictly alternate between positive and negative.
# The first difference (if one exists) may be either positive or
# negative. A sequence with fewer than two elements is trivially a
# wiggle sequence.

# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the
# differences (6, -3, 5, -7, 3) are alternately positive and negative.

# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle
# sequences, the first because its first two differences are positive
# and the second because its last difference is zero.

# A subsequence is obtained by deleting some elements (eventually, also
# zero) from the original sequence, leaving the remaining elements in
# their original order.


# Example 1:
# Input: nums = [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.

# Example 2:
# Input: nums = [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

# Example 3:
# Input: nums = [1,2,3,4,5,6,7,8,9]
# Output: 2

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000

# Follow up: Could you solve this in O(n) time?

from typing import List
from utils import checkValue


class Solution:
    # Memory O(1)
    def wiggleMaxLength(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2:
            return l
        res = 1
        tail, pre = 0, -1
        for i in range(1, l):
            n = nums[i]
            if n - nums[tail] == 0:
                continue
            elif n - nums[tail] > 0:
                if pre >= 0 and nums[tail] - nums[pre] > 0:
                    continue
                if i + 1 < l and nums[i + 1] - n >= 0:
                    continue
            elif n - nums[tail] < 0:
                if pre >= 0 and nums[tail] - nums[pre] < 0:
                    continue
                if i + 1 < l and nums[i + 1] - n <= 0:
                    continue
            res, pre, tail = res + 1, tail, i
        return res

    # Memory O(n)
    def wiggleMaxLength2(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2:
            return l
        res = nums[:1]
        for i, n in enumerate(nums[1:]):
            if n - res[-1] > 0:
                if len(res) > 2 and res[-1] - res[-2] > 0:
                    continue
                if i + 2 < l and nums[i + 2] - n >= 0:
                    continue
                res.append(n)
            elif n - res[-1] < 0:
                if len(res) > 2 and res[-1] - res[-2] < 0:
                    continue
                if i + 2 < l and nums[i + 2] - n <= 0:
                    continue
                res.append(n)
        return len(res)


t = Solution()
checkValue(6, t.wiggleMaxLength([1, 7, 4, 9, 2, 5]))
checkValue(7, t.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
checkValue(2, t.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]))
checkValue(1, t.wiggleMaxLength([1]))
checkValue(0, t.wiggleMaxLength([]))
checkValue(5, t.wiggleMaxLength([10, 8, 10, 15, 10, 15]))
checkValue(5, t.wiggleMaxLength([1, 20, 30, 29, 30, 29]))
checkValue(6, t.wiggleMaxLength([1, 20, 19, 8, 7, 9, 2, 5]))
