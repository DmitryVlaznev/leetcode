# 1043. Partition Array for Maximum Sum

# Medium

# Given an integer array arr, partition the array into (contiguous)
# subarrays of length at most k. After partitioning, each subarray has
# their values changed to become the maximum value of that subarray.

# Return the largest sum of the given array after partitioning. Test
# cases are generated so that the answer fits in a 32-bit integer.


# Example 1:
# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: arr becomes [15,15,15,9,10,10,10]

# Example 2:
# Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# Output: 83

# Example 3:
# Input: arr = [1], k = 1
# Output: 1


# Constraints:
# 1 <= arr.length <= 500
# 0 <= arr[i] <= 10^9
# 1 <= k <= arr.length

from typing import List
from functools import cache


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        @cache
        def dp(start):
            if start == len(arr):
                return 0

            nonlocal k

            local_max, res = float("-inf"), 0
            for i in range(k):
                if start + i == len(arr):
                    break
                local_max = max(local_max, arr[start + i])
                rest = dp(start + i + 1)
                res = max(res, local_max * (i + 1) + rest)
            return res

        return dp(0)


s = Solution()
s.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3)
