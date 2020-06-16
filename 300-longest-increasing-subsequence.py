# 300. Longest Increasing Subsequence

# Given an unsorted array of integers, find the length of longest
# increasing subsequence.

# Example:
# Input: [10,9,2,5,3,7,101,18]
# Output: 4

# Explanation: The longest increasing subsequence is [2,3,7,101],
# therefore the length is 4.

# Note:
# There may be more than one LIS combination, it is only necessary for
# you to return the length.
# Your algorithm should run in O(n^2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not len(nums): return 0

        dp = [1] * len(nums)
        res = 1
        for i, n in enumerate(nums):
            for j in range(i):
                if n > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(dp[i], res)
        return res

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(4, t.lengthOfLIS([10,9,2,5,3,7,101,18]))
log(0, t.lengthOfLIS([]))
log(5, t.lengthOfLIS([1,9,2,5,2,7,2,101,18]))
log(1, t.lengthOfLIS([0]))
log(2, t.lengthOfLIS([0, 1]))
log(1, t.lengthOfLIS([1, 0]))
log(1, t.lengthOfLIS([13, 6, 6, 3]))
