# 605. Can Place Flowers

# Easy

# You have a long flowerbed in which some of the plots are planted, and
# some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means
# empty and 1 means not empty, and an integer n, return if n new flowers
# can be planted in the flowerbed without violating the
# no-adjacent-flowers rule.


# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

# Constraints:
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

from typing import List
from utils import checkValue


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n > len(flowerbed):
            return False
        for i in range(0, len(flowerbed)):
            if flowerbed[i]:
                continue
            l = flowerbed[i - 1] if i > 0 else 0
            r = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
            if n > 0 and l + r == 0:
                flowerbed[i] = 1
                n -= 1
        return n == 0


t = Solution()
checkValue(True, t.canPlaceFlowers([1, 0, 0, 0, 1], 1))
checkValue(False, t.canPlaceFlowers([1, 0, 0, 0, 1], 2))
checkValue(True, t.canPlaceFlowers([], 0))
checkValue(True, t.canPlaceFlowers([0], 1))
checkValue(False, t.canPlaceFlowers([1], 1))
checkValue(False, t.canPlaceFlowers([], 1))

checkValue(True, t.canPlaceFlowers([0, 0, 1], 1))
checkValue(True, t.canPlaceFlowers([1, 0, 0], 1))
checkValue(True, t.canPlaceFlowers([1, 0, 0, 0, 0, 0, 0], 1))
