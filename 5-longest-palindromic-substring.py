# 5. Longest Palindromic Substring

# Medium

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Example 3:
# Input: s = "a"
# Output: "a"

# Example 4:
# Input: s = "ac"
# Output: "a"

# Constraints:
# * 1 <= s.length <= 1000
# * s consist of only digits and English letters (lower-case and/or
#   upper-case),

from utils import checkValue


class Solution:
    def findLongest(self, l: int, r: int, s: str):
        res, start, end = r - l + 1, l, r
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res, start, end = r - l + 1, l, r
            l, r = l - 1, r + 1
        return res, start, end

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        res, start, end = 1, 0, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                nn, ll, rr = self.findLongest(i, i - 1, s)
                if nn > res:
                    res, start, end = nn, ll, rr
            if i < len(s) - 1 and s[i - 1] == s[i + 1]:
                nn, ll, rr = self.findLongest(i, i, s)
                if nn > res:
                    res, start, end = nn, ll, rr
        return s[start : end + 1]


t = Solution()

checkValue("bab", t.longestPalindrome("babad"))
checkValue("bb", t.longestPalindrome("cbbdse"))
checkValue("bb", t.longestPalindrome("bbdse"))
checkValue("bb", t.longestPalindrome("cbb"))
checkValue("cbbc", t.longestPalindrome("qwecbbcse"))
checkValue("cbbc", t.longestPalindrome("cbbcse"))
checkValue("cbbc", t.longestPalindrome("qwecbbc"))
checkValue("cbebc", t.longestPalindrome("qwecbebcr"))
checkValue("cbebc", t.longestPalindrome("cbebcr"))
checkValue("cbebc", t.longestPalindrome("qwecbebc"))
checkValue("cbebc", t.longestPalindrome("cbebc"))
checkValue("cbbc", t.longestPalindrome("cbbc"))
checkValue("bb", t.longestPalindrome("bb"))
checkValue("b", t.longestPalindrome("b"))
checkValue("qwertrewq", t.longestPalindrome("qwertrewq"))
checkValue("ccc", t.longestPalindrome("ccc"))
checkValue("cccc", t.longestPalindrome("cccc"))
checkValue("ccccc", t.longestPalindrome("ccccc"))