# 1685. Sum of Absolute Differences in a Sorted Array

# Medium

# You are given an integer array nums sorted in non-decreasing order.

# Build and return an integer array result with the same length as nums
# such that result[i] is equal to the summation of absolute differences
# between nums[i] and all the other elements in the array.

# In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0
# <= j < nums.length and j != i (0-indexed).


# Example 1:
# Input: nums = [2,3,5]
# Output: [4,3,5]
# Explanation: Assuming the arrays are 0-indexed, then
# result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
# result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
# result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.

# Example 2:
# Input: nums = [1,4,6,8,10]
# Output: [24,15,13,15,21]

# Constraints:
# 2 <= nums.length <= 10^5
# 1 <= nums[i] <= nums[i + 1] <= 10^4

from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        r_sum, l, acc = [0] * len(nums), len(nums), 0
        for i in range(l - 1, -1, -1):
            r_sum[i] = acc
            acc += nums[i]

        res = []
        acc = 0
        for i in range(l):
            res.append(i * nums[i] - acc)
            res[-1] += r_sum[i] - (l - i - 1) * nums[i]
            acc += nums[i]

        return res


from utils import checkList

s = Solution()
checkList([4, 3, 5], s.getSumAbsoluteDifferences([2, 3, 5]))
checkList([24, 15, 13, 15, 21], s.getSumAbsoluteDifferences([1, 4, 6, 8, 10]))
