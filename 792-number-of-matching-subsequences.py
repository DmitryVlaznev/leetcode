# 792. Number of Matching Subsequences

# Medium

# Given a string s and an array of strings words, return the number of
# words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original
# string with some characters (can be none) deleted without changing the
# relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".


# Example 1:
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

# Example 2:
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2


# Constraints:
# 1 <= s.length <= 5 * 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.

from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res, heads = 0, [[] for _ in range(26)]
        for w in words:
            heads[ord(w[0]) - ord("a")].append(w)
        for l in s:
            i = ord(l) - ord("a")
            bucket = heads[i]
            heads[i] = []
            for w in bucket:
                if len(w) == 1:
                    res += 1
                else:
                    nw = w[1:]
                    heads[ord(nw[0]) - ord("a")].append(nw)
        return res