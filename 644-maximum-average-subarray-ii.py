# 644. Maximum Average Subarray II

# Hard

# You are given an integer array nums consisting of n elements, and an
# integer k.

# Find a contiguous subarray whose length is greater than or equal to k
# that has the maximum average value and return this value. Any answer
# with a calculation error less than 10-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation:
# - When the length is 4, averages are [0.5, 12.75, 10.5] and the
#   maximum average is 12.75
# - When the length is 5, averages are [10.4, 10.8] and the maximum
#   average is 10.8
# - When the length is 6, averages are [9.16667] and the maximum average
#   is 9.16667
# The maximum average is when we choose a subarray of length 4 (i.e.,
# the sub array [12, -5, -6, 50]) which has the max average 12.75, so we
# return 12.75
# Note that we do not consider the subarrays of length < 4.

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000

# Constraints:
# n == nums.length
# 1 <= k <= n <= 104
# -104 <= nums[i] <= 104

from typing import List
from utils import checkValue


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_val, min_val = max(nums), min(nums)
        prev_mid, err = max_val, float("inf")

        while err > 0.00001:
            mid = min_val + (max_val - min_val) / 2
            if self.check(nums, mid, k):
                min_val = mid
            else:
                max_val = mid
            err = abs(prev_mid - mid)
            prev_mid = mid
        return min_val

    def check(self, nums: List[int], mid: float, k: int) -> bool:
        s = sum(nums[0:k]) - mid * k
        if s > 0:
            return True

        prev = min_sum = 0
        for i in range(k, len(nums)):
            s += nums[i] - mid
            prev += nums[i - k] - mid
            min_sum = min(prev, min_sum)
            if s >= min_sum:
                return True
        return False
