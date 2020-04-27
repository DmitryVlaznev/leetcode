# 55. Jump Game

# Given an array of non-negative integers, you are initially positioned
# at the first index of the array.

# Each element in the array represents your maximum jump length at that
# position.

# Determine if you are able to reach the last index.

# Example 1:
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = max(len(nums) - 1, 0)
        p = target - 1
        while p >= 0:
            if p + nums[p] - target >= 0:
                target = p
            p -= 1
        return target == 0


t = Solution()
print("True = ", t.canJump([2,3,1,1,4]))
print("False = ", t.canJump([3,2,1,0,4]))
print("False = ", t.canJump([0,2]))
print("True = ", t.canJump([0]))
print("True = ", t.canJump([]))
print("True = ", t.canJump([34,0,0,0,4]))
print("True = ", t.canJump([2,0,0]))