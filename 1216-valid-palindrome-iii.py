# 1216. Valid Palindrome III

# Hard

# Given a string s and an integer k, return true if s is a k-palindrome.

# A string is k-palindrome if it can be transformed into a palindrome by
# removing at most k characters from it.

# Example 1:
# Input: s = "abcdeca", k = 2
# Output: true
# Explanation: Remove 'b' and 'e' characters.

# Example 2:
# Input: s = "abbababa", k = 1
# Output: true


# Constraints:
# 1 <= s.length <= 1000
# s consists of only lowercase English letters.
# 1 <= k <= s.length


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

    def isValidPalindrome(self, s: str, k: int) -> bool:
        return len(s) - self.longest(s, 0, len(s) - 1) <= k


s = Solution()
checkValue(True, s.isValidPalindrome("abcdeca", 2))
checkValue(True, s.isValidPalindrome("abbababa", 1))