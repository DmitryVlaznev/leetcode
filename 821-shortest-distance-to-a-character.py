# 821. Shortest Distance to a Character

# Easy

# Given a string s and a character c that occurs in s, return an array
# of integers answer where answer.length == s.length and answer[i] is
# the shortest distance from s[i] to the character c in s.

# Example 1:
# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]

# Example 2:
# Input: s = "aaab", c = "b"
# Output: [3,2,1,0]

# Constraints:
# 1 <= s.length <= 104
# s[i] and c are lowercase English letters.
# c occurs at least once in s.

from typing import List
from utils import checkList


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l = len(s)
        res = [None] * l
        last = None
        for i in range(l - 1, -1, -1):
            if s[i] == c:
                res[i], last = 0, i
            elif last is not None:
                res[i] = last - i
        last = None
        for i in range(0, l):
            if s[i] == c:
                last = i
            elif last is not None:
                res[i] = min(res[i], i - last) if res[i] is not None else i - last
        return res


t = Solution()

checkList([3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0], t.shortestToChar("loveleetcode", "e"))
checkList([3, 2, 1, 0], t.shortestToChar("aaab", "b"))
checkList([2, 1, 0, 1], t.shortestToChar("aaba", "b"))
checkList([0], t.shortestToChar("b", "b"))
