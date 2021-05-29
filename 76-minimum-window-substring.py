# 76. Minimum Window Substring

# Hard

# Given two strings s and t of lengths m and n respectively, return the
# minimum window in s which will contain all the characters in t. If
# there is no such window in s that covers all characters in t, return
# the empty string "".

# Note that If there is such a window, it is guaranteed that there will
# always be only one unique minimum window in s.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"

# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s and t consist of English letters.

# Follow up: Could you find an algorithm that runs in O(m + n) time?

from utils import checkValue

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 1 and t[0] in s:
            return t
        sample = Counter(t)
        sample_letters, diff = set(sample.keys()), len(sample.keys())
        seen = {k: 0 for k in sample_letters}
        p = q = 0
        res, res_slice = float("inf"), [-1, -1]

        while p < len(s):
            if s[p] in sample_letters:
                seen[s[p]] += 1
                if seen[s[p]] == sample.get(s[p]):
                    diff = max(diff - 1, 0)

                if diff == 0:
                    while q < p:
                        if s[q] in sample_letters:
                            if seen[s[q]] == sample.get(s[q]):
                                break
                            else:
                                seen[s[q]] -= 1
                        q += 1
                    if res > p - q:
                        res = p - q
                        res_slice = [q, p]
            p += 1

        if res == float("inf"):
            return ""
        return s[res_slice[0] : res_slice[1] + 1]


t = Solution()
checkValue("BANC", t.minWindow("ADOBECODEBANC", "ABC"))
checkValue("a", t.minWindow("aqwe", "a"))
checkValue("a", t.minWindow("deaawe", "a"))
checkValue("aa", t.minWindow("deaaaaawe", "aa"))
checkValue("aea", t.minWindow("deaeaeaeaeawe", "aa"))
checkValue("ba", t.minWindow("bba", "ab"))
checkValue("aab", t.minWindow("aab", "aab"))