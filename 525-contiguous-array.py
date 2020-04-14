# Contiguous Array

# Given a binary array, find the maximum length of a contiguous subarray
# with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal
# number of 0 and 1.

# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with
# equal number of 0 and 1.

# Note: The length of the given binary array will not exceed 50,000.

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        l = len(nums)
        sums = {0: -1}
        max_length = cur_sum = p = 0
        while p < l:
            cur_sum = cur_sum + 1 if nums[p] == 1 else cur_sum - 1
            if cur_sum in sums:
                max_length = max(max_length, p - sums[cur_sum])
            else:
                sums[cur_sum] = p
            p += 1

        return max_length

t = Solution()

print("2 = ", t.findMaxLength([0, 1, 1]))
print("2 = ", t.findMaxLength([0, 1]))
print("2 = ", t.findMaxLength([0, 1, 0]))
print("4 = ", t.findMaxLength([1, 1, 1, 0, 0, 1, 1]))
print("6 = ", t.findMaxLength([1, 1, 1, 0, 0, 0]))
print("0 = ", t.findMaxLength([0, 0]))



