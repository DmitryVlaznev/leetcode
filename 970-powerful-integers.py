# 970. Powerful Integers

# Medium

# Given three integers x, y, and bound, return a list of all the
# powerful integers that have a value less than or equal to bound.

# An integer is powerful if it can be represented as x^i + y^j for some
# integers i >= 0 and j >= 0.

# You may return the answer in any order. In your answer, each value
# should occur at most once.


# Example 1:
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation:
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2

# Example 2:
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]

# Constraints:
# 1 <= x, y <= 100
# 0 <= bound <= 10^6

from typing import List
from utils import checkList


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        yy = [1]
        if y > 1:
            c = 1
            while c < bound:
                yy.append(c)
                c *= y
        res = set()
        c = 1
        while c < bound:
            p = 0
            while p < len(yy) and c + yy[p] <= bound:
                res.add(c + yy[p])
                p += 1
            c *= x if x > 1 else float("inf")
        return list(res)


t = Solution()

checkList([2, 3, 4, 5, 7, 9, 10], sorted(t.powerfulIntegers(2, 3, 10)))
checkList([2, 4, 6, 8, 10, 14], sorted(t.powerfulIntegers(3, 5, 15)))
checkList([], sorted(t.powerfulIntegers(3, 5, 0)))
checkList([], sorted(t.powerfulIntegers(3, 5, 1)))
checkList([2], sorted(t.powerfulIntegers(3, 5, 2)))
checkList([2], sorted(t.powerfulIntegers(3, 5, 2)))
checkList([2, 3, 5, 9, 17, 33, 65], sorted(t.powerfulIntegers(1, 2, 100)))
