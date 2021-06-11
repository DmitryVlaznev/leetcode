# 164. Maximum Gap

# Hard

# Given an integer array nums, return the maximum difference between two
# successive elements in its sorted form. If the array contains less
# than two elements, return 0.

# You must write an algorithm that runs in linear time and uses linear
# extra space.

# Example 1:
# Input: nums = [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6)
# or (6,9) has the maximum difference 3.

# Example 2:
# Input: nums = [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return
# 0.

# Constraints:

# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^9

from typing import List
from utils import checkValue


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        elif len(nums) == 2:
            return max(nums) - min(nums)

        minBuckets = [float("inf")] * len(nums)
        maxBuckets = [-1] * len(nums)
        left, right = min(nums), max(nums)
        if left == right:
            return 0
        size = max((right - left) // (len(nums) - 1), 1)

        for n in nums:
            bucket = min((n - left) // size, len(nums) - 1)
            minBuckets[bucket] = min(minBuckets[bucket], n)
            maxBuckets[bucket] = max(maxBuckets[bucket], n)

        res, lastMax = 0, maxBuckets[0]
        for i in range(1, len(nums)):
            if maxBuckets[i] == -1:
                continue
            res = max(res, minBuckets[i] - lastMax)
            lastMax = maxBuckets[i]
        return res


t = Solution()
checkValue(3, t.maximumGap([1, 3, 6, 9]))
checkValue(0, t.maximumGap([1, 1, 1, 1]))
checkValue(1, t.maximumGap([1, 1, 1, 1, 1, 1, 2]))
checkValue(97, t.maximumGap([100, 3, 2, 1]))
