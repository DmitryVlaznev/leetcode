# Perform String Shifts

# You are given a string s containing lowercase English letters, and a
# matrix shift, where shift[i] = [direction, amount]:
# direction can be 0 (for left shift) or 1 (for right shift).
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it
# to the end.
# Similarly, a right shift by 1 means remove the last character of s and
# add it to the beginning.
# Return the final string after all operations.

# Example 1:
# Input: s = "abc", shift = [[0,1],[1,2]]
# Output: "cab"
# Explanation:
# [0,1] means shift to left by 1. "abc" -> "bca"
# [1,2] means shift to right by 2. "bca" -> "cab"

# Example 2:
# Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
# Output: "efgabcd"
# Explanation:
# [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
# [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
# [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
# [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


# Constraints:
# 1 <= s.length <= 100
# s only contains lower case English letters.
# 1 <= shift.length <= 100
# shift[i].length == 2
# 0 <= shift[i][0] <= 1
# 0 <= shift[i][1] <= 100

from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if not len(s): return s

        actual_shift = 0
        for step in shift:
            actual_shift = actual_shift - step[1] if step[0] == 0 else actual_shift + step[1]
        if actual_shift == 0: return s

        d = -1 if actual_shift < 0 else 1
        actual_shift = abs(actual_shift) % len(s)

        if d > 0:
            return s[-actual_shift:] + s[0:-actual_shift]
        else:
            return s[actual_shift:] + s[0:actual_shift]

t = Solution()
print("cab => ", t.stringShift("abc", [[0,1],[1,2]]))
print("abc => ", t.stringShift("abc", [[0,1],[1,2], [0,1]]))
print("efgabcd => ", t.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]))

print("yisxjwry => ", t.stringShift("yisxjwry", [[1,8],[1,4],[1,3],[1,6],[0,6],[1,4],[0,2],[0,1]]))

