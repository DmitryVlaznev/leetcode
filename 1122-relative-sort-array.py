# 1122. Relative Sort Array

# Easy

# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and
# all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in
# arr1 are the same as in arr2. Elements that do not appear in arr2
# should be placed at the end of arr1 in ascending order.


# Example 1:
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

# Example 2:
# Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
# Output: [22,28,8,6,17,44]


# Constraints:

# 1 <= arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# All the elements of arr2 are distinct.
# Each arr2[i] is in arr1.

from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        res = []
        for n in arr2:
            res += [n] * c[n]
            c.pop(n)
        rest = []
        for n in c.keys():
            rest += [n] * c[n]
        return res + sorted(rest)


s = Solution()

from utils import checkList

checkList(
    [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
    s.relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]),
)
checkList(
    [22, 28, 8, 6, 17, 44], s.relativeSortArray([28, 6, 22, 8, 44, 17], [22, 28, 8, 6])
)

# checkList([2], s.relativeSortArray([2], [2]))

checkList(
    [2, 42, 38, 0, 43, 21, 5, 7, 12, 12, 13, 23, 24, 24, 27, 29, 30, 31, 33, 48],
    s.relativeSortArray(
        [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31],
        [2, 42, 38, 0, 43, 21],
    ),
)
