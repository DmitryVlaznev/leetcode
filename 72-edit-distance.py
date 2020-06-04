# 72. Edit Distance

# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.

# You have the following 3 operations permitted on a word:
# * Insert a character
# * Delete a character
# * Replace a character

# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'l2' with 'x')
# exention -> exection (replace 'l2' with 'c')
# exection -> execution (insert 'u')

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Create a table to store results of subproblems
        l1, l2 = len(word1), len(word2)
        dp = [[0 for x in range(l2 + 1)] for x in range(l1 + 1)]

        # Fill d[][] bottom up manner
        for i in range(l1 + 1):
            for j in range(l2 + 1):
                # If first string is empty, only option is to
                # insert all characters of second string
                if i == 0: dp[i][j] = j    # Min. operations = j

                # If second string is empty, only option is to
                # remove all characters of second string
                elif j == 0: dp[i][j] = i    # Min. operations = i

                # If last characters are same, ignore last char
                # and recur for remaining string
                elif word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]

                # If last character are different, consider all
                # possibilities and find minimum
                else: dp[i][j] = 1 + min(
                    dp[i][j-1],        # Insert
                    dp[i-1][j],        # Remove
                    dp[i-1][j-1])      # Replace
        return dp[l1][l2]


def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log(3, t.minDistance("horse", "ros"))
log(5, t.minDistance("intention", "execution"))
log(1, t.minDistance("", "e"))
log(0, t.minDistance("", ""))
log(0, t.minDistance("qwe", "qwe"))
log(3, t.minDistance("sea", "ate"))