# 1272. Remove Interval

# Medium

# Given a sorted list of disjoint intervals, each interval intervals[i]
# = [a, b] represents the set of real numbers x such that a <= x < b.

# We remove the intersections between any interval in intervals and the
# interval toBeRemoved.

# Return a sorted list of intervals after all such removals.


# Example 1:
# Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
# Output: [[0,1],[6,7]]

# Example 2:
# Input: intervals = [[0,5]], toBeRemoved = [2,3]
# Output: [[0,2],[3,5]]

# Example 3:
# Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
# Output: [[-5,-4],[-3,-2],[4,5],[8,9]]

# Constraints:

# 1 <= intervals.length <= 10^4
# -10^9 <= intervals[i][0] < intervals[i][1] <= 10^9

from typing import List
from utils import checkList


class Solution:
    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:
        res = []
        for i in intervals:
            if i[0] >= toBeRemoved[0] and i[1] <= toBeRemoved[1]:
                # remove
                continue
            elif i[0] >= toBeRemoved[1] or i[1] <= toBeRemoved[0]:
                # take full
                res.append(i)
            elif toBeRemoved[0] > i[0] and toBeRemoved[1] < i[1]:
                # divide in two
                res.append([i[0], toBeRemoved[0]])
                res.append([toBeRemoved[1], i[1]])
            else:
                # truncate
                start = i[0] if i[0] < toBeRemoved[0] else toBeRemoved[1]
                end = i[1] if i[1] > toBeRemoved[1] else toBeRemoved[0]
                res.append([start, end])
        return res
