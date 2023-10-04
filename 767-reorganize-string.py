# 767. Reorganize String

# Medium

# Given a string s, rearrange the characters of s so that any two
# adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.


# Example 1:
# Input: s = "aab"
# Output: "aba"

# Example 2:
# Input: s = "aaab"
# Output: ""

# Constraints:
# 1 <= s.length <= 500
# s consists of lowercase English letters.

from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        l, n = c.most_common(1)[0]
        d = len(s) % 2
        if n * 2 > len(s) + d:
            return ""

        res, p = [None] * len(s), 0
        left = lambda p, l: p == 0 or res[p - 1] != l
        right = lambda p, l: p == len(res) - 1 or res[p + 1] != l
        for l, n in c.most_common():
            while n:
                if res[p] is None and left(p, l) and right(p, l):
                    res[p] = l
                    n -= 1
                else:
                    p = 0 if p == len(s) - 1 else p + 1
        return "".join(res)


s = Solution()
print(s.reorganizeString("bbbaaaa"))
