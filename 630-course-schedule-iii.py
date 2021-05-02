# 630. Course Schedule III

# Hard

# There are n different online courses numbered from 1 to n. You are
# given an array courses where courses[i] = [durationi, lastDayi]
# indicate that the ith course should be taken continuously for
# durationi days and must be finished before or on lastDayi.

# You will start on the 1st day and you cannot take two or more courses
# simultaneously.

# Return the maximum number of courses that you can take.

# Example 1:
# Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# Output: 3
# Explanation:
# There are totally 4 courses, but you can take 3 courses at most:
# First, take the 1st course, it costs 100 days so you will finish it on
# the 100th day, and ready to take the next course on the 101st day.
# * Second, take the 3rd course, it costs 1000 days so you will finish
#   it on the 1100th day, and ready to take the next course on the
#   1101st day.
# * Third, take the 2nd course, it costs 200 days so you will finish it
#   on the 1300th day.
# * The 4th course cannot be taken now, since you will finish it on the
#   3300th day, which exceeds the closed date.

# Example 2:
# Input: courses = [[1,2]]
# Output: 1

# Example 3:
# Input: courses = [[3,2],[4,3]]
# Output: 0

# Constraints:
# 1 <= courses.length <= 104
# 1 <= durationi, lastDayi <= 104

from typing import List
from utils import checkValue
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda course: course[1])

        res, days, taken = 0, 0, []
        for duration, last in courses:
            if days + duration <= last:
                days += duration
                res += 1
                heapq.heappush(taken, -duration)
            elif taken:
                if abs(taken[0]) > duration:
                    days = days + taken[0] + duration
                    heapq.heappushpop(taken, -duration)

        return res


t = Solution()

checkValue(3, t.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
checkValue(2, t.scheduleCourse([[100, 2], [10, 28], [5, 14]]))
checkValue(3, t.scheduleCourse([[100, 2], [4, 5], [1, 5], [2, 5], [5, 10]]))
checkValue(1, t.scheduleCourse([[1, 2]]))
checkValue(1, t.scheduleCourse([[1, 2]]))
checkValue(0, t.scheduleCourse([[3, 2], [4, 3]]))
checkValue(2, t.scheduleCourse([[5, 5], [4, 6], [2, 6]]))
