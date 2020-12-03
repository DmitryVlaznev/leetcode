# 243. Shortest Word Distance

# Easy

# Given a list of words and two words word1 and word2, return the
# shortest distance between these two words in the list.

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Input: word1 = “coding”, word2 = “practice”
# Output: 3

# Input: word1 = "makes", word2 = "coding"
# Output: 1

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2
# are both in the list.

from typing import List
from utils import checkValue


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        words_hash = {}
        for i, word in enumerate(words):
            if word in words_hash:
                words_hash[word].append(i)
            else:
                words_hash[word] = [i]
        idx1, idx2 = words_hash[word1], words_hash[word2]

        p, q, distance = 0, 0, float("inf")
        while p < len(idx1) and q < len(idx2):
            i1 = idx1[p] if p < len(idx1) else idx1[-1]
            i2 = idx2[q] if q < len(idx2) else idx2[-1]
            distance = min(distance, abs(i1 - i2))
            if i1 < i2:
                if p < len(idx1):
                    p += 1
                else:
                    q += 1
            else:
                if q < len(idx2):
                    q += 1
                else:
                    p += 1
        return distance


t = Solution()

checkValue(
    3,
    t.shortestDistance(
        ["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"
    ),
)
checkValue(
    1,
    t.shortestDistance(
        ["practice", "makes", "perfect", "coding", "makes"], "coding", "makes"
    ),
)
checkValue(
    1,
    t.shortestDistance(
        ["practice", "makes", "perfect", "coding", "makes"],
        "makes",
        "coding",
    ),
)
checkValue(
    1,
    t.shortestDistance(["a", "c", "c", "b", "b", "b", "a"], "a", "b"),
)

checkValue(
    1,
    t.shortestDistance(["a", "c"], "a", "c"),
)