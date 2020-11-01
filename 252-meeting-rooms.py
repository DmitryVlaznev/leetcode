# 252. Meeting Rooms

# Given an array of meeting time intervals where intervals[i] =
# [start_i, end_i], determine if a person could attend all meetings.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true

# Constraints:
# 0 <= intervals.length <= 104
# intervals.length == 2
# 0 <= start_i < end_i <= 106

from typing import List
from utils import checkValue


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda i: i[0])
        for i in range(0, len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


t = Solution()
checkValue(False, t.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
checkValue(True, t.canAttendMeetings([[7, 10], [2, 4]]))
checkValue(True, t.canAttendMeetings([[4, 10], [2, 4]]))
checkValue(False, t.canAttendMeetings([[4, 10], [2, 8]]))
checkValue(False, t.canAttendMeetings([[4, 10], [2, 8]]))
checkValue(True, t.canAttendMeetings([]))
