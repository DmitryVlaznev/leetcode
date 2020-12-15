# 131. Palindrome Partitioning

# Medium

# Given a string s, partition s such that every substring of the
# partition is a palindrome. Return all possible palindrome partitioning
# of s.

# A palindrome string is a string that reads the same backward as
# forward.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.

from typing import List


class Solution:
    def is_palindrome(self, s: str, start_index: int, end_index: int):
        while start_index < end_index:
            if s[start_index] != s[end_index]:
                return False
            start_index += 1
            end_index -= 1
        return True

    def get_palindrome(self, s: str, start_index: int, min_length: int):
        p = start_index + min_length - 1
        while p < len(s):
            if self.is_palindrome(s, start_index, p):
                return p + 1
            p += 1
        return -1

    def backtrack(self, s: str, res: List[List[str]], cur: List[str], start_index: int):
        if start_index == len(s):
            if not cur in res:
                res.append(cur[:])
            return

        for l in range(1, len(s) - start_index + 1):
            rest = self.get_palindrome(s, start_index, l)
            if rest != -1:
                nxt = cur[:]
                nxt.append(s[start_index:rest])
                self.backtrack(s, res, nxt, rest)
            else:
                return

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtrack(s, res, [], 0)
        return res


t = Solution()
print(t.partition("aab"))
print(t.partition("abc"))
print(t.partition("a"))
print(t.partition("abcb"))