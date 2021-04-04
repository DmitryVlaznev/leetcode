# 16. 3Sum Closest

# Medium

# Given an array nums of n integers and an integer target, find three
# integers in nums such that the sum is closest to target. Return the
# sum of the three integers. You may assume that each input would have
# exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 =
# 2).

# Constraints:
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4

from typing import List
from utils import checkValue


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff, res = float("inf"), None
        nums.sort()
        for i in range(0, len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(target - s) < diff:
                    diff, res = abs(target - s), s
                if s <= target:
                    j += 1
                if s >= target:
                    k -= 1
        return res


t = Solution()

checkValue(2, t.threeSumClosest([-1, 2, 1, -4], 1))
checkValue(0, t.threeSumClosest([-1, 0, 1, 2, -1, -4], 0))
checkValue(-1, t.threeSumClosest([1, 1, -1, -1, 3], -1))
