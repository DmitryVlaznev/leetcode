# 593. Valid Square

# Given the coordinates of four points in 2D space, return whether the
# four points could construct a square.

# The coordinate (x,y) of a point is represented by an integer array
# with two integers.

# Example:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True

# Note:
# * All the input integers are in the range [-10000, 10000].
# * A valid square has four equal sides with positive length and four
#   equal angles (90-degree angles).
# * Input points have no order.

from typing import List
from utils import checkValue


class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        import math

        l = []
        l.append(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))
        l.append(math.sqrt((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2))
        l.append(math.sqrt((p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2))
        l.append(math.sqrt((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2))
        l.append(math.sqrt((p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2))
        l.append(math.sqrt((p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2))

        l.sort()

        return l[0] != 0 and l[0] == l[1] == l[2] == l[3] and l[4] == l[5]


t = Solution()
checkValue(True, t.validSquare([0, 0], [1, 1], [1, 0], [0, 1]))
checkValue(False, t.validSquare([0, 0], [0, 0], [0, 0], [0, 0]))
