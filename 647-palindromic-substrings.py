# 647. Palindromic Substrings

# Medium

# Given a string, your task is to count how many palindromic substrings
# in this string.

# The substrings with different start indexes or end indexes are counted
# as different substrings even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: "aaa"
# Output: 6

# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Note:
# The input string length won't exceed 1000.


class Solution:
    def countSubstrings(self, s: str) -> int:
        res, l = 0, len(s)

        # check odds
        for i in range(l):
            p = q = i
            while p >= 0 and q < l and s[p] == s[q]:
                res = res + 1 if s[p : q + 1] else res
                p, q = p - 1, q + 1
        # check evens
        for i in range(l - 1):
            p, q = i, i + 1
            while p >= 0 and q < l and s[p] == s[q]:
                res = res + 1 if s[p : q + 1] else res
                p, q = p - 1, q + 1
        return res


t = Solution()
print(t.countSubstrings("abc"))
print(t.countSubstrings("aaa"))
print(t.countSubstrings("abcdcba"))
print(t.countSubstrings("xabceece"))
