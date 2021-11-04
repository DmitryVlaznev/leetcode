# 698. Partition to K Equal Sum Subsets

# Medium

# Solution

# Given an integer array nums and an integer k, return true if it is
# possible to divide this array into k non-empty subsets whose sums are
# all equal.

# Example 1:
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4),
# (2,3), (2,3) with equal sums.

# Example 2:
# Input: nums = [1,2,3,4], k = 3
# Output: false

# Constraints:

# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 10^4
# The frequency of each element is in the range [1, 4].

from typing import List


class Solution:
    # TLE
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k or len(nums) < k:
            return False

        s = sum(nums) // k

        def placeItem(item, buckets):
            nonlocal s
            if item == len(nums):
                for n in buckets:
                    if n != s:
                        return False
                return True

            v = nums[item]
            for i in range(len(buckets)):
                if buckets[i] + v > s:
                    continue

                buckets[i] += v
                if placeItem(item + 1, buckets):
                    return True
                buckets[i] -= v
            return False

        return placeItem(0, [0] * k)