# 318. Maximum Product of Word Lengths

# Medium

# Given a string array words, return the maximum value of
# length(word[i]) * length(word[j]) where the two words do not share
# common letters. If no such two words exist, return 0.

# Example 1:
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".

# Example 2:
# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".

# Example 3:
# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.

# Constraints:
# 2 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists only of lowercase English letters.

from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmasks = []
        for word in words:
            b = 0
            for l in word:
                letter_mask = 1 << (ord(l) - ord("a"))
                b = b | letter_mask
            bitmasks.append(b)
        res = 0
        for p in range(0, len(bitmasks) - 1):
            for q in range(p + 1, len(bitmasks)):
                if not bitmasks[p] & bitmasks[q]:
                    res = max(res, len(words[p]) * len(words[q]))
        return res


t = Solution()
t.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
