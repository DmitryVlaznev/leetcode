# 1288. Remove Covered Intervals

# Given a list of intervals, remove all intervals that are covered by
# another interval in the list.

# Interval [a,b) is covered by interval [c,d) if and only if c <= a and
# b <= d.

# After doing so, return the number of remaining intervals.

# Example 1:
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is
# removed.

# Example 2:
# Input: intervals = [[1,4],[2,3]]
# Output: 1

# Example 3:
# Input: intervals = [[0,10],[5,12]]
# Output: 2

# Example 4:
# Input: intervals = [[3,10],[4,10],[5,11]]
# Output: 2

# Example 5:
# Input: intervals = [[1,2],[1,4],[3,4]]
# Output: 1

# Constraints:
# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= intervals[i][0] < intervals[i][1] <= 10^5
# All the intervals are unique.

from typing import List
import utils


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        import functools
        def comparator(a, b):
            if a[0] < b[0]: return -1
            if a[0] > b[0]: return 1
            if a[1] > b[1]: return -1
            if a[1] < b[1]: return 1
            return 0
        intervals.sort(key=functools.cmp_to_key(comparator))

        res = len(intervals)
        sample, p = 0, 1
        while p < len(intervals):
            if intervals[sample][0] <= intervals[p][0] and intervals[sample][1] >= intervals[p][1]: res -= 1
            else: sample = p
            p += 1
        return res



t = Solution()
utils.checkValue(2, t.removeCoveredIntervals([[1,4],[3,6],[2,8]]))
utils.checkValue(1, t.removeCoveredIntervals([[1,4],[2,3]]))
utils.checkValue(2, t.removeCoveredIntervals([[0,10],[5,12]]))
utils.checkValue(2, t.removeCoveredIntervals([[3,10],[4,10],[5,11]]))
utils.checkValue(1, t.removeCoveredIntervals([[1,2],[1,4],[3,4]]))