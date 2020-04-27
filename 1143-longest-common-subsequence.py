# 1143. Longest Common Subsequence

# Given two strings text1 and text2, return the length of their longest
# common subsequence.

# A subsequence of a string is a new string generated from the original
# string with some characters(can be none) deleted without changing the
# relative order of the remaining characters. (eg, "ace" is a
# subsequence of "abcde" while "aec" is not). A common subsequence of
# two strings is a subsequence that is common to both strings.

# If there is no common subsequence, return 0.

# Example 1:
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

# Constraints:
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0] * l1 for i in range(l2)]
        for p2 in range(0, l2):
            for p1 in range(0, l1):
                if text1[p1] == text2[p2]:
                    dp[p2][p1] = dp[p2-1][p1-1] + 1 if p1 > 0 and p2 > 0 else 1
                else:
                    up = dp[p2 - 1][p1] if p2 > 0 else 0
                    left = dp[p2][p1 - 1] if p1 > 0 else 0
                    dp[p2][p1] = max(up, left)
        return dp[l2 - 1][l1 - 1]

t = Solution()
print("3 = ", t.longestCommonSubsequence("abcde", "ace"))
print("3 = ", t.longestCommonSubsequence("abc", "abc"))
print("0 = ", t.longestCommonSubsequence("abc", "def"))
print("7 = ", t.longestCommonSubsequence("axyzbklmcde", "acexzblce"))

print("1 = ", t.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))

