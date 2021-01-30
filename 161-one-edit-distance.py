# 161. One Edit Distance

# Medium

# Given two strings s and t, return true if they are both one edit
# distance apart, otherwise return false.

# A string s is said to be one distance apart from a string t if you can:
# * Insert exactly one character into s to get t.
# * Delete exactly one character from s to get t.
# * Replace exactly one character of s with a different character to get t.


# Example 1:
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.

# Example 2:
# Input: s = "", t = ""
# Output: false
# Explanation: We cannot get t from s by only one step.

# Example 3:
# Input: s = "a", t = ""
# Output: true

# Example 4:
# Input: s = "", t = "A"
# Output: true


# Constraints:
# 0 <= s.length <= 104
# 0 <= t.length <= 104
# s and t consist of lower-case letters, upper-case letters and/or digits.

from utils import checkValue


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        if len(s) == len(t):
            # we can only replace
            replaced = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    replaced += 1
                    if replaced > 1:
                        return False
        else:
            # we can only insert or remove
            short = s if len(s) <= len(t) else t
            long = t if short == s else s
            p = q = 0
            inserted = 0
            while p < len(short) and q < len(long):
                if short[p] != long[q]:
                    q += 1
                    inserted += 1
                    if inserted > 1:
                        return False
                else:
                    p += 1
                    q += 1
        return True


t = Solution()

checkValue(True, t.isOneEditDistance("ab", "acb"))
checkValue(False, t.isOneEditDistance("", ""))
checkValue(True, t.isOneEditDistance("a", ""))
checkValue(True, t.isOneEditDistance("", "A"))
checkValue(True, t.isOneEditDistance("qwerty", "qwert"))
checkValue(True, t.isOneEditDistance("werty", "qwerty"))
checkValue(True, t.isOneEditDistance("qwery", "qwerty"))
checkValue(True, t.isOneEditDistance("qwerty", "qwery"))
checkValue(True, t.isOneEditDistance("qwewty", "qwerty"))

checkValue(False, t.isOneEditDistance("qwewty", "qwertt"))
checkValue(False, t.isOneEditDistance("qwerty", "qwer"))
checkValue(False, t.isOneEditDistance("qwerty", "qwerjh"))
checkValue(False, t.isOneEditDistance("qwe", "qwe"))
