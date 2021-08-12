# 132. Palindrome Partitioning II

# Hard

# Given a string s, partition s such that every substring of the
# partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced
# using 1 cut.

# Example 2:
# Input: s = "a"
# Output: 0

# Example 3:
# Input: s = "ab"
# Output: 1

# Constraints:
# 1 <= s.length <= 2000
# s consists of lower-case English letters only.

from functools import lru_cache
from utils import checkValue

# O(N*3) TLE


class Solution:
    def minCut(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def isPalindrome(start: int, end: int):
            nonlocal s

            while start < end:
                if s[start] != s[end]:
                    return False
                start, end = start + 1, end - 1
            return True

        @lru_cache(maxsize=None)
        def minCutPartial(start, end):
            if isPalindrome(start, end):
                return 0

            res = float("inf")
            for p in range(start, end):
                res = min(
                    res,
                    1 + minCutPartial(start, p) + minCutPartial(p + 1, end),
                )
            return res

        return minCutPartial(0, len(s) - 1)


# O(N*3) TLE

# class Solution:
#     def minCut(self, s: str) -> int:
#         n = len(s)
#         memoPal = [[None] * n for _ in range(0, n)]

#         def isPalindrome(start: int, end: int):
#             nonlocal s
#             if memoPal[start][end] is not None:
#                 return memoPal[start][end]

#             mid = (end - start) // 2
#             l, r = start + mid, start + mid + (end - start) % 2
#             while l >= start and s[l] == s[r]:
#                 memoPal[l][r] = True
#                 l, r = l - 1, r + 1
#             return l == start - 1

#         @lru_cache(maxsize=None)
#         def minCutPartial(start, end):
#             if isPalindrome(start, end):
#                 return 0

#             res = float("inf")
#             for p in range(start, end):
#                 res = min(
#                     res,
#                     1 + minCutPartial(start, p) + minCutPartial(p + 1, end),
#                 )
#             return res

#         return minCutPartial(0, len(s) - 1)

# O(N*3) TLE

# class Solution:
#     def isPalindrome(self, s, start: int, end: int):
#         if self.memoPal[start][end] is not None:
#             return self.memoPal[start][end]

#         mid = (end - start) // 2
#         l, r = start + mid, start + mid + (end - start) % 2
#         while l >= start and s[l] == s[r]:
#             self.memoPal[l][r] = True
#             l, r = l - 1, r + 1
#         return l == start - 1

#     def minCutPartial(self, s, start, end):
#         if self.memoCut[start][end] is not None:
#             return self.memoCut[start][end]

#         if self.isPalindrome(s, start, end):
#             self.memoCut[start][end] = 0
#             return 0

#         res = float("inf")
#         for p in range(start, end):
#             res = min(
#                 res,
#                 1 + self.minCutPartial(s, start, p) + self.minCutPartial(s, p + 1, end),
#             )
#         self.memoCut[start][end] = res
#         return res

#     def minCut(self, s: str) -> int:
#         n = len(s)
#         self.memoCut = [[None] * n for _ in range(0, n)]
#         self.memoPal = [[None] * n for _ in range(0, n)]
#         return self.minCutPartial(s, 0, len(s) - 1)


# O(N*2) Babichev

# from collections import defaultdict

# class Solution:
#     def minCut(self, s):
#         d, n = defaultdict(set), len(s)

#         def helper(i, j):
#             while i >= 0 and j < n and s[i] == s[j]:
#                 d[i].add(j)
#                 i, j = i - 1, j + 1

#         for k in range(n):
#             helper(k, k)
#             helper(k, k + 1)

#         @lru_cache(None)
#         def dp(i):
#             if i == -1:
#                 return 0
#             return min([dp(k - 1) + 1 for k in range(0, i + 1) if i in d[k]])

#         return dp(n - 1) - 1


import sys

sys.setrecursionlimit(1000000)

s = Solution()

str = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
# str = "aab"
checkValue(452, s.minCut(str))