# 1539. Kth Missing Positive Number

# Easy

# Given an array arr of positive integers sorted in a strictly
# increasing order, and an integer k.

# Find the kth positive integer that is missing from this array.

# Example 1:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9

# Explanation: The missing positive integers are
# [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

# Example 2:
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd
# missing positive integer is 6.


# Constraints:
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length

from typing import List
from utils import checkValue


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = -1, len(arr)
        while r - l > 1:
            mid = l + (r - l) // 2
            if arr[mid] - mid - 1 < k:
                l = mid
            else:
                r = mid
        if l == -1:
            return k
        return arr[l] + k - (arr[l] - l - 1)


t = Solution()

checkValue(9, t.findKthPositive([2, 3, 4, 7, 11], 5))
checkValue(6, t.findKthPositive([1, 2, 3, 4], 2))
checkValue(2, t.findKthPositive([4], 2))
checkValue(5, t.findKthPositive([4], 4))
checkValue(4, t.findKthPositive([], 4))
