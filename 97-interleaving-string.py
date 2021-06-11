# 97. Interleaving String

# Medium

# Given strings s1, s2, and s3, find whether s3 is formed by an
# interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where they
# are divided into non-empty substrings such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1

# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2
# + s2 + t3 + s3 + ...

# Note: a + b is the concatenation of strings a and b.

# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

# Example 2:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false

# Example 3:
# Input: s1 = "", s2 = "", s3 = ""
# Output: true

# Constraints:
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.

# Follow up: Could you solve it using only O(s2.length) additional
# memory space?

from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(maxsize=None)
        def dp(i1: int, i2: int, i3: int):
            nonlocal s1, s2, s3
            if i1 == len(s1) and i2 == len(s2):
                return True
            if i3 == len(s3):
                return False

            c1 = dp(i1 + 1, i2, i3 + 1) if i1 < len(s1) and s1[i1] == s3[i3] else False
            c2 = dp(i1, i2 + 1, i3 + 1) if i2 < len(s2) and s2[i2] == s3[i3] else False
            return c1 or c2

        return dp(0, 0, 0) if len(s1) + len(s2) == len(s3) else False
