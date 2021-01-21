# 1658. Minimum Operations to Reduce X to Zero

# Medium

# You are given an integer array nums and an integer x. In one
# operation, you can either remove the leftmost or the rightmost element
# from the array nums and subtract its value from x. Note that this
# modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if
# it's possible, otherwise, return -1.


# Example 1:
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements
# to reduce x to zero.

# Example 2:
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1

# Example 3:
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements
# and the first two elements (5 operations in total) to reduce x to
# zero.


# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# 1 <= x <= 109

from typing import List
from utils import checkValue


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        if s < x:
            return -1
        if s == x:
            return len(nums)
        target = s - x
        p, q = 0, 0
        arrSum = maxLength = 0
        while p < len(nums):
            arrSum += nums[p]
            while arrSum > target and q < p:
                arrSum -= nums[q]
                q += 1
            if arrSum == target:
                maxLength = max(maxLength, p - q + 1)
            p += 1
        return -1 if maxLength == 0 else len(nums) - maxLength


t = Solution()

checkValue(2, t.minOperations([1, 1, 4, 2, 3], 5))
checkValue(-1, t.minOperations([5, 6, 7, 8, 9], 4))
checkValue(5, t.minOperations([3, 2, 20, 1, 1, 3], 10))
checkValue(1, t.minOperations([10, 2, 20, 1, 1, 3], 10))
checkValue(1, t.minOperations([2, 20, 1, 1, 3, 10], 10))
checkValue(3, t.minOperations([2, 20, 1, 10, 3, 4, 3], 10))
checkValue(-1, t.minOperations([1, 10, 3], 10))
checkValue(-1, t.minOperations([1, 1], 3))
checkValue(
    16,
    t.minOperations(
        [
            8828,
            9581,
            49,
            9818,
            9974,
            9869,
            9991,
            10000,
            10000,
            10000,
            9999,
            9993,
            9904,
            8819,
            1231,
            6309,
        ],
        134365,
    ),
)
