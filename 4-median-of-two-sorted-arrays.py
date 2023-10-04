# 4. Median of Two Sorted Arrays

# Hard

# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6

from typing import List


class Solution:
    # O(m+n) solution, not  O(log (m+n))
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # For 0-based indices, If l1 + l2 is odd, we are looking for the
        # (l1 + l2) // 2-th element. If l1 + l2 is even, we are
        # looking for the average of the (l1 + l2) // 2 - 1-th and the
        # (l1 + l2) // 2-th elements.
        l1, l2 = len(nums1), len(nums2)
        i_target1, i_target2 = ((l1 + l2) // 2) - 1, (l1 + l2) // 2
        target1, target2 = 0, 0
        i, p1, p2 = 0, 0, 0
        while i <= i_target2:
            if p1 < l1 and p2 < l2:
                if nums1[p1] < nums2[p2]:
                    v = nums1[p1]
                    p1 += 1
                else:
                    v = nums2[p2]
                    p2 += 1
            elif p1 < l1:
                v = nums1[p1]
                p1 += 1
            else:
                v = nums2[p2]
                p2 += 1

            target1 = v if i_target1 == i else target1
            target2 = v if i_target2 == i else target2
            i += 1

        if (l1 + l2) % 2:
            return target2
        return (target1 + target2) / 2


s = Solution()
# s.findMedianSortedArrays([1, 3], [2])
s.findMedianSortedArrays([1, 2], [3, 4])
