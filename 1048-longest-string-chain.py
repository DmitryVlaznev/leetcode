# 1048. Longest String Chain

# Given a list of words, each word consists of English lowercase
# letters.

# Let's say word1 is a predecessor of word2 if and only if we can add
# exactly one letter anywhere in word1 to make it equal to word2.  For
# example, "abc" is a predecessor of "abac".

# A word chain is a sequence of words [word_1, word_2, ..., word_k] with
# k >= 1, where word_1 is a predecessor of word_2, word_2 is a
# predecessor of word_3, and so on.

# Return the longest possible length of a word chain with words chosen
# from the given list of words.


# Example 1:
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".


# Note:
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.

from typing import List
from functools import lru_cache


class Solution:
    def isPredecessor(self, p: str, c: str):
        if len(c) - len(p) != 1:
            return False
        i = j = 0
        skipped = False
        while i < len(p):
            if p[i] == c[j]:
                i, j = i + 1, j + 1
            elif not skipped:
                skipped, j = True, j + 1
            else:
                return False
        return True

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: len(w))
        dp = [1] * (len(words) + 1)
        for i, word in enumerate(words):
            for j in range(i):
                if self.isPredecessor(words[j], word):
                    dp[i + 1] = dp[j + 1] + 1
        return max(dp)

    # Top-Down DP
    def longestStrChainTDDP(self, words: List[str]) -> int:
        @lru_cache(maxsize=None)
        def dfs(word):
            if len(word) == 1:
                return 1

            res = 0
            for i in range(len(word)):
                candidate = word[0:i] + word[i + 1 :]
                if candidate in words:
                    res = max(res, dfs(candidate))
            return res + 1

        words = set(words)
        res = 1
        for word in words:
            res = max(res, dfs(word))
        return res


def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log(True, t.isPredecessor("a", "ba"))
log(True, t.isPredecessor("a", "ab"))
log(4, t.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))
log(4, t.longestStrChain(["bdca", "a", "bda", "b", "ba", "bca"]))
log(
    5,
    t.longestStrChain(
        ["a", "b", "ba", "ksqar", "bca", "bda", "bdca", "ka", "ksa", "ksqa"]
    ),
)
log(1, t.longestStrChain(["a"]))

words = [
    "ksqvsyq",
    "ks",
    "kss",
    "czvh",
    "zczpzvdhx",
    "zczpzvh",
    "zczpzvhx",
    "zcpzvh",
    "zczvh",
    "gr",
    "grukmj",
    "ksqvsq",
    "gruj",
    "kssq",
    "ksqsq",
    "grukkmj",
    "grukj",
    "zczpzfvdhx",
    "gru",
]
log(7, t.longestStrChain(words))