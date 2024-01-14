# 1287. Element Appearing More Than 25% In Sorted Array

# Easy

# Given an integer array sorted in non-decreasing order, there is
# exactly one integer in the array that occurs more than 25% of the
# time, return that integer.

# Example 1:
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6

# Example 2:
# Input: arr = [1,1]
# Output: 1

# Constraints:
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5

from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return arr[0]
        quarter, mul, cand = (len(arr) // 4), 1, set()
        while mul <= 4 and mul * quarter < len(arr):
            cand.add(arr[mul * quarter - 1])
            cand.add(arr[mul * quarter])
            mul += 1

        for n in cand:
            left_index, right_index = -1, -1

            l, r = -1, len(arr)
            while r - l > 1:
                mid = l + (r - l) // 2
                if arr[mid] < n:
                    l = mid
                else:
                    r = mid
            left_index = r

            l, r = -1, len(arr)
            while r - l > 1:
                mid = l + (r - l) // 2
                if arr[mid] <= n:
                    l = mid
                else:
                    r = mid
            right_index = l

            if right_index - left_index >= quarter:
                return n
        return -1
