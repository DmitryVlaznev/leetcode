# 45. Jump Game II

# Medium

# Given an array of non-negative integers nums, you are initially
# positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that
# position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.


# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 10^5

from typing import List
from utils import checkValue


class Solution:
    # DP O(n^2)
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(0, i):
                if i - j <= nums[j]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]

    # Greedy O(n)
    def jump2(self, nums: List[int]) -> int:
        jumps = 0
        current_jump_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            # we continuously find the how far we can reach in the current jump
            farthest = max(farthest, i + nums[i])
            # if we have come to the end of the current jump,
            # we need to make another jump
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        return jumps


t = Solution()

checkValue(2, t.jump([2, 3, 1, 1, 4]))
checkValue(2, t.jump([2, 3, 0, 1, 4]))
