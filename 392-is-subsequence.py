# 392. Is Subsequence
# Given a string s and a string t, check if s is subsequence of t.

# A subsequence of a string is a new string which is formed from the
# original string by deleting some (can be none) of the characters
# without disturbing the relative positions of the remaining characters.
# (ie, "ace" is a subsequence of "abcde" while "aec" is not).

# Follow up:

# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
# and you want to check one by one to see if T has its subsequence. In
# this scenario, how would you change your code?

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# Both strings consists only of lowercase characters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]: sp += 1
            tp += 1
        return sp == len(s)

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(False, t.isSubsequence("axc", "ahbgdc"))
log(False, t.isSubsequence("aaa", "aa"))
log(True, t.isSubsequence("abc", "ahbgdc"))
log(True, t.isSubsequence("aa", "aaa"))