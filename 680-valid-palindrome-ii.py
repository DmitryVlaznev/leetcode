# 680. Valid Palindrome II

# Easy

# Given a string s, return true if the s can be palindrome after
# deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false


# Constraints:
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, start: int, end: int):
            while start < end:
                if s[start] != s[end]:
                    return False
                start, end = start + 1, end - 1
            return True

        p, q = 0, len(s) - 1
        while p < q:
            if s[p] == s[q]:
                p, q = p + 1, q - 1
            else:
                return isPalindrome(s, p + 1, q) or isPalindrome(s, p, q - 1)
        return True