# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

# Medium

# Given a rectangular cake with height h and width w, and two arrays of
# integers horizontalCuts and verticalCuts where horizontalCuts[i] is
# the distance from the top of the rectangular cake to the ith
# horizontal cut and similarly, verticalCuts[j] is the distance from the
# left of the rectangular cake to the jth vertical cut.

# Return the maximum area of a piece of cake after you cut at each
# horizontal and vertical position provided in the arrays horizontalCuts
# and verticalCuts. Since the answer can be a huge number, return this
# modulo 10^9 + 7.

# Example 1:
# Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# Output: 4
# Explanation: The figure above represents the given rectangular cake.
# Red lines are the horizontal and vertical cuts. After you cut the
# cake, the green piece of cake has the maximum area.

# Example 2:
# Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
# Output: 6
# Explanation: The figure above represents the given rectangular cake.
# Red lines are the horizontal and vertical cuts. After you cut the
# cake, the green and yellow pieces of cake have the maximum area.

# Example 3:
# Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
# Output: 9

# Constraints:
# 2 <= h, w <= 10^9
# 1 <= horizontalCuts.length < min(h, 10^5)
# 1 <= verticalCuts.length < min(w, 10^5)
# 1 <= horizontalCuts[i] < h
# 1 <= verticalCuts[i] < w
# It is guaranteed that all elements in horizontalCuts are distinct.
# It is guaranteed that all elements in verticalCuts are distinct.

from typing import List
from utils import checkValue


class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        def maxGap(arr, high):
            size = max(1, high // len(arr) + 1)
            buckets = [None] * (high // size + 1)
            for n in arr:
                i = n // size
                if not buckets[i]:
                    buckets[i] = [n, n]
                else:
                    buckets[i][0] = min(buckets[i][0], n)
                    buckets[i][1] = max(buckets[i][1], n)
            res, last = 0, 0
            for b in buckets:
                if not b:
                    continue
                res = max(res, b[0] - last)
                last = b[1]
            res = max(res, high - last)
            return res

        vg = maxGap(horizontalCuts, h)
        hg = maxGap(verticalCuts, w)
        return (hg * vg) % (10 ** 9 + 7)


s = Solution()

checkValue(4, s.maxArea(5, 4, [1, 2, 4], [1, 3]))
checkValue(6, s.maxArea(5, 4, [3, 1], [1]))
checkValue(9, s.maxArea(5, 4, [3], [3]))
checkValue(6, s.maxArea(8, 5, [5, 2, 6, 3], [1, 4]))
