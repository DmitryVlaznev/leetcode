# 681. Next Closest Time

# Medium

# Given a time represented in the format "HH:MM", form the next closest
# time by reusing the current digits. There is no limit on how many
# times a digit can be reused.

# "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
# You may assume the given input string is always valid. For example,


# Example 1:
# Input: time = "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
# It is not 19:33, because this occurs 23 hours and 59 minutes later.

# Example 2:
# Input: time = "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.


# Constraints:

# time.length == 5
# time is a valid time in the form "HH:MM".
# 0 <= HH < 24
# 0 <= MM < 60


class Solution:
    def nextClosestTime(self, time: str) -> str:
        def generate(minimum, maximum, digits):
            res = float("inf")
            for i in digits:
                for j in digits:
                    cand = int(i + j)
                    if cand >= minimum and cand <= maximum:
                        res = min(res, cand)
            return res if res < float("inf") else -1

        digits = set([time[0], time[1], time[3], time[4]])
        hh = int(time[0:2])
        mm = int(time[3:])

        hours = hh
        minutes = generate(mm + 1, 59, digits)
        if minutes == -1:
            minutes = generate(0, 59, digits)
            hours = generate(hh + 1, 23, digits)
            if hours == -1:
                hours = generate(0, 23, digits)

        hours = str(hours) if hours > 9 else "0" + str(hours)
        minutes = str(minutes) if minutes > 9 else "0" + str(minutes)
        return hours + ":" + minutes


from utils import checkValue

s = Solution()
checkValue("19:39", s.nextClosestTime("19:34"))
checkValue("22:22", s.nextClosestTime("23:59"))
