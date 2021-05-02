# 1229. Meeting Scheduler

# Medium

# Given the availability time slots arrays slots1 and slots2 of two
# people and a meeting duration duration, return the earliest time slot
# that works for both of them and is of duration duration.

# If there is no common time slot that satisfies the requirements,
# return an empty array.

# The format of a time slot is an array of two elements [start, end]
# representing an inclusive time range from start to end.

# It is guaranteed that no two availability slots of the same person
# intersect with each other. That is, for any two time slots [start1,
# end1] and [start2, end2] of the same person, either start1 > end2 or
# start2 > end1.

# Example 1:
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# Output: [60,68]

# Example 2:
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
# Output: []

# Constraints:
# 1 <= slots1.length, slots2.length <= 10^4
# slots1[i].length, slots2[i].length == 2
# slots1[i][0] < slots1[i][1]
# slots2[i][0] < slots2[i][1]
# 0 <= slots1[i][j], slots2[i][j] <= 10^9
# 1 <= duration <= 10^6

from typing import List
from utils import checkList


class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        slots1.sort(key=lambda s: s[0])
        slots2.sort(key=lambda s: s[0])
        slots1.append([float("inf"), float("inf")])
        slots2.append([float("inf"), float("inf")])

        p1 = p2 = 0
        while p1 < len(slots1) - 1 and p2 < len(slots2) - 1:
            s1, e1 = slots1[p1]
            s2, e2 = slots2[p2]

            s, e = max(s1, s2), min(e1, e2)
            if e - s >= duration:
                return [s, s + duration]
            if slots1[p1 + 1][0] < slots2[p2 + 1][0]:
                p1 += 1
            else:
                p2 += 1
        return []


t = Solution()

checkList(
    [60, 68],
    t.minAvailableDuration([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8),
)
checkList(
    [],
    t.minAvailableDuration([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12),
)
