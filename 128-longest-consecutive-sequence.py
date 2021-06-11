# 128. Longest Consecutive Sequence

# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3,
# 4]. Therefore its length is 4.

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h, res = set(nums), 0
        for n in nums:
            if n - 1 not in h:
                l = 0
                while n in h:
                    n += 1
                    l += 1
                res = max(res, l)
        return res


test = Solution()
print("4 = ", test.longestConsecutive([100, 4, 200, 1, 3, 2]))
print("0 = ", test.longestConsecutive([]))
print("1 = ", test.longestConsecutive([1, 6, 42]))
print("2 = ", test.longestConsecutive([-2, -1, 42]))
print("3 = ", test.longestConsecutive([15, -1, 42, 0, 1]))
