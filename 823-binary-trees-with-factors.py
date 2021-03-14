# 823. Binary Trees With Factors

# Medium

# Given an array of unique integers, arr, where each integer arr[i] is
# strictly greater than 1.

# We make a binary tree using these integers, and each number may be
# used for any number of times. Each non-leaf node's value should be
# equal to the product of the values of its children.

# Return the number of binary trees we can make. The answer may be too
# large so return the answer modulo 10^9 + 7.

# Example 1:
# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]

# Example 2:
# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2],
# [10, 2, 5], [10, 5, 2].

# Constraints:
# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 109

from typing import List
from utils import checkValue


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        arr.sort()
        dp = [1] * len(arr)
        indices = {n: i for i, n in enumerate(arr)}
        for i, n in enumerate(arr):
            for ai, a in enumerate(arr[0:i]):
                if n % a != 0:
                    continue
                b = n / a
                if b in indices:
                    bi = indices[b]
                    dp[i] += dp[ai] * dp[bi] % mod
        res = 0
        for n in dp:
            res = (res + n) % mod
        return res


t = Solution()

checkValue(18, t.numFactoredBinaryTrees([2, 3, 4, 6, 12]))
checkValue(3, t.numFactoredBinaryTrees([2, 4]))
checkValue(7, t.numFactoredBinaryTrees([2, 4, 5, 10]))
