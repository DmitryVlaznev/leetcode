# 88. Merge Sorted Array

# Easy

# Given two sorted integer arrays nums1 and nums2, merge nums2 into
# nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n
# respectively. You may assume that nums1 has enough space (size that is
# equal to m + n) to hold additional elements from nums2.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]

# Constraints:
# 0 <= n, m <= 200
# 1 <= n + m <= 200
# nums1.length == m + n
# nums2.length == n
# -109 <= nums1[i], nums2[i] <= 109

from typing import List
from utils import checkList


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m - 1, -1, -1):
            nums1[i + n] = nums1[i]
        k1 = n
        k2 = p = 0
        while p < m + n:
            if k1 < m + n and k2 < n:
                if nums1[k1] <= nums2[k2]:
                    nums1[p] = nums1[k1]
                    k1 += 1
                else:
                    nums1[p] = nums2[k2]
                    k2 += 1
            elif k1 < m + n:
                nums1[p] = nums1[k1]
                k1 += 1
            else:
                nums1[p] = nums2[k2]
                k2 += 1
            p += 1


t = Solution()

arr1 = [1, 2, 3, 0, 0, 0]
arr2 = [2, 5, 6]
t.merge(arr1, 3, arr2, 3)
checkList([1, 2, 2, 3, 5, 6], arr1)

arr1 = [1]
arr2 = []
t.merge(arr1, 1, arr2, 0)
checkList([1], arr1)

arr1 = [0]
arr2 = [2]
t.merge(arr1, 0, arr2, 1)
checkList([2], arr1)

arr1 = []
arr2 = []
t.merge(arr1, 0, arr2, 0)
checkList([], arr1)

arr1 = [1, 2, 3, 0, 0, 0, 0]
arr2 = [4, 5, 6, 7]
t.merge(arr1, 3, arr2, 4)
checkList([1, 2, 3, 4, 5, 6, 7], arr1)

arr1 = [4, 5, 6, 7, 0, 0, 0]
arr2 = [1, 2, 3]
t.merge(arr1, 4, arr2, 3)
checkList([1, 2, 3, 4, 5, 6, 7], arr1)