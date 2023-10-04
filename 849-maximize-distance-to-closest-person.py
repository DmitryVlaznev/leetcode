# 849. Maximize Distance to Closest Person

# You are given an array representing a row of seats where seats[i] = 1
# represents a person sitting in the ith seat, and seats[i] = 0
# represents that the ith seat is empty (0-indexed).

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and
# the closest person to him is maximized.

# Return that maximum distance to the closest person.

# Example 1:
# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# * If Alex sits in the second open seat (i.e. seats[2]), then the
#   closest person has distance 2.
# * If Alex sits in any other open seat, the closest person has distance
#   1.
# * Thus, the maximum distance to the closest person is 2.

# Example 2:
# Input: seats = [1,0,0,0]
# Output: 3
# Explanation:
# * If Alex sits in the last seat (i.e. seats[3]), the closest person is
#   3 seats away.
# * This is the maximum distance possible, so the answer is 3.

# Example 3:
# Input: seats = [0,1]
# Output: 1

# Constraints:
# 2 <= seats.length <= 2 * 104
# seats[i] is 0 or 1.
# At least one seat is empty.
# At least one seat is occupied.

from typing import List
from utils import checkValue


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ltr = [float("inf")] * len(seats)
        ltr[0] = 0 if seats[0] == 1 else float("inf")
        for i in range(1, len(seats)):
            ltr[i] = 0 if seats[i] == 1 else ltr[i - 1] + 1

        rtl = [float("inf")] * len(seats)
        rtl[-1] = 0 if seats[-1] == 1 else float("inf")
        for i in reversed(range(0, len(seats) - 1)):
            rtl[i] = 0 if seats[i] == 1 else rtl[i + 1] + 1

        res = float("-inf")
        for i in range(0, len(seats)):
            if ltr[i] == rtl[i] == 0:
                continue
            res = max(res, min(ltr[i], rtl[i]))
        return res

    def maxDistToClosest2(self, seats: List[int]) -> int:
        p, max_side_gap, max_int_gap = 0, 0, 0
        while not seats[p]:
            max_side_gap += 1
            p += 1

        q = len(seats) - 1
        while not seats[q]:
            max_side_gap = max(max_side_gap, len(seats) - q)
            q -= 1

        s = None
        while p < q:
            if seats[p]:
                if s is not None:
                    max_int_gap = max(max_int_gap, p - s)
                    s = None
            else:
                if s is None:
                    s = p
            p += 1

        if s is not None:
            max_int_gap = max(max_int_gap, p - s)
        import math

        return max(max_side_gap, math.ceil(max_int_gap / 2))

        # print("max_side_gap", max_side_gap)
        # print("max_int_gap", max_int_gap)


t = Solution()
checkValue(2, t.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
checkValue(2, t.maxDistToClosest([1, 0, 1, 0, 0, 0, 1]))
checkValue(2, t.maxDistToClosest([1, 0, 0, 0, 0, 1, 0, 1]))
checkValue(2, t.maxDistToClosest([1, 0, 1, 0, 0, 0, 0, 1]))
checkValue(3, t.maxDistToClosest([1, 0, 0, 0]))
checkValue(3, t.maxDistToClosest([0, 0, 0, 1]))
checkValue(1, t.maxDistToClosest([0, 1]))
checkValue(1, t.maxDistToClosest([1, 0]))
checkValue(3, t.maxDistToClosest([0, 0, 0, 1, 0, 0]))
checkValue(3, t.maxDistToClosest([0, 0, 1, 0, 0, 0]))
