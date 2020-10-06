# 56. Merge Intervals

# Given a collection of intervals, merge all overlapping intervals.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.


# Constraints:
# intervals[i][0] <= intervals[i][1]

from typing import List
from utils import checkList

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return intervals

        import functools
        def comparator(a, b):
            if a[0] < b[0]: return -1
            if a[0] > b[0]: return 1
            if a[1] > b[1]: return -1
            if a[1] < b[1]: return 1
            return 0
        intervals.sort(key=functools.cmp_to_key(comparator))

        res = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if cur[1] < intervals[i][0]:
                res.append(cur)
                cur = intervals[i]
            elif cur[1] < intervals[i][1]:
                cur[1] = intervals[i][1]
        res.append(cur)
        return res

t = Solution()

checkList([[1,6],[8,10],[15,18]], t.merge([[1,3],[2,6],[8,10],[15,18]]))
checkList([[1,6],[8,10],[15,18]], t.merge([[8,10],[2,6],[1,3],[15,18]]))
checkList([[1,5]], t.merge([[1,4],[4,5]]))
checkList([[1,24]], t.merge([[1,24],[4,5]]))
checkList([], t.merge([]))