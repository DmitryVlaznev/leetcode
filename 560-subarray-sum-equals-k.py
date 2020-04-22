# 560. Subarray Sum Equals K

# Given an array of integers and an integer k, you need to find the
# total number of continuous subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2

# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {}
        res = 0
        cur = 0
        for n in nums:
            cur += n
            if cur == k: res += 1
            diff = cur - k
            if diff in sums: res += sums[diff]
            sums[cur] = sums[cur] + 1 if cur in sums else 1

        return res

t = Solution()
print("2 = ", t.subarraySum([1,1,1], 2))
print("3 = ", t.subarraySum([1,1,1], 1))
print("4 = ", t.subarraySum([1,2,-2,5,-6,1], 0))
print("2 = ", t.subarraySum([1,2,-2,5,-6,1], -1))