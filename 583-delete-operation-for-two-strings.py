# 583. Delete Operation for Two Strings

# Medium

# Given two strings word1 and word2, return the minimum number of steps
# required to make word1 and word2 the same.

# In one step, you can delete exactly one character in either string.

# Example 1:
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step
# to make "eat" to "ea".

# Example 2:
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4


# Constraints:
# 1 <= word1.length, word2.length <= 500
# word1 and word2 consist of only lowercase English letters.


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0] * l1 for i in range(l2)]
        for p2 in range(0, l2):
            for p1 in range(0, l1):
                if word1[p1] == word2[p2]:
                    dp[p2][p1] = dp[p2 - 1][p1 - 1] + 1 if p1 > 0 and p2 > 0 else 1
                else:
                    up = dp[p2 - 1][p1] if p2 > 0 else 0
                    left = dp[p2][p1 - 1] if p1 > 0 else 0
                    dp[p2][p1] = max(up, left)
        return l1 + l2 - 2 * dp[l2 - 1][l1 - 1]