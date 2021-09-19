# 978. Longest Turbulent Subarray

# Medium

# Given an integer array arr, return the length of a maximum size
# turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each
# adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is
# said to be turbulent if and only if:

# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.

# Example 1:
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

# Example 2:
# Input: arr = [4,8,12,16]
# Output: 2

# Example 3:
# Input: arr = [100]
# Output: 1

# Constraints:
# 1 <= arr.length <= 4 * 10^4
# 0 <= arr[i] <= 10^9

from typing import List
from utils import checkValue


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def compare(a, b):
            return 1 if a > b else -1 if a < b else 0

        res, start = 1, 0
        for i in range(1, len(arr)):
            c = compare(arr[i - 1], arr[i])
            if c == 0:
                start = i
            elif i == len(arr) - 1 or c * compare(arr[i], arr[i + 1]) != -1:
                res = max(res, i - start + 1)
                start = i
        return res


s = Solution()
checkValue(5, s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
checkValue(1, s.maxTurbulenceSize([9]))
checkValue(1, s.maxTurbulenceSize([9, 9]))
checkValue(1, s.maxTurbulenceSize([9, 9, 9]))
checkValue(1, s.maxTurbulenceSize([9, 9, 9, 9]))
checkValue(2, s.maxTurbulenceSize([4, 8, 12, 16]))
checkValue(5, s.maxTurbulenceSize([1, 2, 3, 1, 2, 1]))
checkValue(3, s.maxTurbulenceSize([1, 5, 4, 3, 2, 1]))
checkValue(8, s.maxTurbulenceSize([0, 8, 45, 88, 48, 68, 28, 55, 17, 24]))
