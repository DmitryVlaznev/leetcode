# 229. Majority Element II

# Medium

# Given an integer array of size n, find all elements that appear more
# than ⌊ n/3 ⌋ times.


# Example 1:
# Input: nums = [3,2,3]
# Output: [3]

# Example 2:
# Input: nums = [1]
# Output: [1]

# Example 3:
# Input: nums = [1,2]
# Output: [1,2]

# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9

# Follow up: Could you solve the problem in linear time and in O(1)
# space?

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict

        target = len(nums) // 3 + 1
        h = defaultdict(lambda: 0)
        res = set()

        for n in nums:
            h[n] += 1
            if h[n] >= target:
                res.add(n)
        return list(res)
