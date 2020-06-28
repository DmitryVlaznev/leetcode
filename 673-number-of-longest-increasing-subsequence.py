# 673. Number of Longest Increasing Subsequence

# Given an unsorted array of integers, find the number of longest
# increasing subsequence.

# Example 1:
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7]
# and [1, 3, 5, 7].

# Example 2:
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence
# is 1, and there are 5 subsequences' length is 1, so output 5.

# Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        count = [1] * len(nums)

        for i, n in enumerate(nums):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] == dp[j] + 1: count[i] += count[j]
                    elif dp[i] < dp[j] + 1:
                        dp[i] += 1
                        count[i] = count[j]
        m = max(dp)
        res = 0
        for i, n in enumerate(dp):
            if n == m:
                res += count[i]
        return res
# print(dp)
# print(count)
def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(2, t.findNumberOfLIS([1,3,5,4,7]))
log(5, t.findNumberOfLIS([2,2,2,2,2]))
log(5, t.findNumberOfLIS([5,4,3,2,1]))
log(2, t.findNumberOfLIS([13,56,75,4,7,9]))
log(1, t.findNumberOfLIS([5]))
log(0, t.findNumberOfLIS([]))
log(27, t.findNumberOfLIS([1,1,1,2,2,2,3,3,3]))
log(1, t.findNumberOfLIS([100,90,80,70,60,50,60,70,80,90,100]))