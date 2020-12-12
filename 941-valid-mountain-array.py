# 941. Valid Mountain Array

# Easy

# Given an array of integers arr, return true if and only if it is a
# valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < A[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


# Example 1:
# Input: arr = [2,1]
# Output: false

# Example 2:
# Input: arr = [3,5,5]
# Output: false

# Example 3:
# Input: arr = [0,3,2,1]
# Output: true


# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104

from typing import List
from utils import checkValue


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        functools.reduce(lambda acc, v, i: acc)

        if len(arr) < 3:
            return False
        state = 0
        for i, n in enumerate(arr[1:]):
            if n == arr[i]:
                return False
            if state == 0 and n < arr[i]:
                return False
            if state == 0 and n > arr[i]:
                state = 1
            if state == 1 and n < arr[i]:
                state = 2
            if state == 2 and n > arr[i]:
                return False
        return state == 2


t = Solution()

checkValue(False, t.validMountainArray([2, 1]))
checkValue(False, t.validMountainArray([3, 5, 5]))
checkValue(False, t.validMountainArray([3, 5, 6, 7, 4, 3, 3, 2]))
checkValue(False, t.validMountainArray([3, 5, 6]))
checkValue(True, t.validMountainArray([0, 3, 2, 1]))
checkValue(True, t.validMountainArray([0, 1, 2, 3, 1]))
checkValue(False, t.validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
checkValue(
    False, t.validMountainArray([2, 1, 2, 3, 5, 7, 9, 10, 12, 14, 15, 16, 18, 14, 13])
)
