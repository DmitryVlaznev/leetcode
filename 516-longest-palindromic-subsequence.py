# 516. Longest Palindromic Subsequence

# Medium

# Given a string s, find the longest palindromic subsequence's length in
# s.

# A subsequence is a sequence that can be derived from another sequence
# by deleting some or no elements without changing the order of the
# remaining elements.

# Example 1:
# Input: s = "bbbab"
# Output: 4

# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".

# Constraints:
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.


from functools import lru_cache
from utils import checkValue


class Solution:
    @lru_cache(maxsize=None)
    def longest(self, s: str, i: int, j: int):
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return 2 + self.longest(s, i + 1, j - 1)
        if s[i] != s[j]:
            return max(self.longest(s, i + 1, j), self.longest(s, i, j - 1))

    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longest(s, 0, len(s) - 1)


s = Solution()

checkValue(4, s.longestPalindromeSubseq("bbbab"))
checkValue(5, s.longestPalindromeSubseq("abcdeca"))
checkValue(7, s.longestPalindromeSubseq("abbababa"))
checkValue(1, s.longestPalindromeSubseq("a"))
checkValue(1, s.longestPalindromeSubseq("ab"))
checkValue(2, s.longestPalindromeSubseq("aa"))
checkValue(5, s.longestPalindromeSubseq("abcba"))