# 551. Student Attendance Record I

# You are given a string representing an attendance record for a
# student. The record only contains the following three characters:

# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.

# A student could be rewarded if his attendance record doesn't contain
# more than one 'A' (absent) or more than two continuous 'L' (late).

# You need to return whether the student could be rewarded according to
# his attendance record.

# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False

from typing import List


class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_count = 0

        for i in range(0, len(s)):
            a_count = a_count + 1 if s[i] == "A" else a_count
            if s[i] == "L":
                if i > 0 and s[i-1] == "L":
                    l_count += 1
                else:
                    l_count = 1

            if a_count > 1 or l_count > 2: return False
        return True

t = Solution()
print("True", t.checkRecord("PPALLP"))
print("False", t.checkRecord("PPALLL"))
print("True", t.checkRecord("LALL"))