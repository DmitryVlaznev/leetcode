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
        if not len(nums):
            return 0

        ht = set();
        for n in nums:
            ht.add(n)

        longest = 1
        for n in nums:
            if (n - 1) in ht:
                continue

            length = 1
            v = n + 1
            while v in ht:
                length +=1
                v += 1

            longest = length if length > longest else longest

        return longest

test = Solution()
print("4 = ", test.longestConsecutive([100, 4, 200, 1, 3, 2]))
print("0 = ", test.longestConsecutive([]))
print("1 = ", test.longestConsecutive([1, 6, 42]))
print("2 = ", test.longestConsecutive([-2, -1, 42]))
print("3 = ", test.longestConsecutive([15, -1, 42, 0, 1]))

