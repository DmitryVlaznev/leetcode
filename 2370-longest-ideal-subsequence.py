# 2370. Longest Ideal Subsequence

# Medium

# You are given a string s consisting of lowercase letters and an
# integer k. We call a string t ideal if the following conditions are
# satisfied:

# t is a subsequence of the string s.
# The absolute difference in the alphabet order of every two adjacent
# letters in t is less than or equal to k.
# Return the length of the longest ideal string.

# A subsequence is a string that can be derived from another string by
# deleting some or no characters without changing the order of the
# remaining characters.

# Note that the alphabet order is not cyclic. For example, the absolute
# difference in the alphabet order of 'a' and 'z' is 25, not 1.


# Example 1:
# Input: s = "acfgbd", k = 2
# Output: 4
# Explanation: The longest ideal string is "acbd". The length of this
# string is 4, so 4 is returned. Note that "acfgbd" is not ideal because
# 'c' and 'f' have a difference of 3 in alphabet order.

# Example 2:
# Input: s = "abcd", k = 3
# Output: 4
# Explanation: The longest ideal string is "abcd". The length of this
# string is 4, so 4 is returned.


# Constraints:
# 1 <= s.length <= 10^5
# 0 <= k <= 25
# s consists of lowercase English letters.


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp, res = [0] * 26, 0
        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            best = 0
            for prev in range(26):
                if abs(prev - curr) <= k:
                    best = max(best, dp[prev])
            dp[curr] = max(dp[curr], best + 1)
            res = max(res, dp[curr])
        return res

    # TLE
    def longestIdealString2(self, s: str, k: int) -> int:
        dp = [1] * len(s)
        for i in range(1, len(s)):
            for j in range(0, i):
                if abs(ord(s[i]) - ord(s[j])) <= k:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
