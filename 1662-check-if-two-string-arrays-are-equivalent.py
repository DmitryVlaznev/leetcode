# 1662. Check If Two String Arrays are Equivalent

# Easy

# Given two string arrays word1 and word2, return true if the two arrays
# represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated
# in order forms the string.


# Example 1:
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

# Example 2:
# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false

# Example 3:
# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true

# Constraints:
# 1 <= word1.length, word2.length <= 103
# 1 <= word1[i].length, word2[i].length <= 103
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 103
# word1[i] and word2[i] consist of lowercase letters.


from typing import List
from utils import checkValue


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = p1 = w2 = p2 = 0
        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][p1] != word2[w2][p2]:
                return False
            p1 = p1 + 1 if p1 < len(word1[w1]) - 1 else 0
            w1 = w1 + 1 if p1 == 0 else w1
            p2 = p2 + 1 if p2 < len(word2[w2]) - 1 else 0
            w2 = w2 + 1 if p2 == 0 else w2
        return w1 == len(word1) and w2 == len(word2)


t = Solution()

checkValue(True, t.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
checkValue(False, t.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
checkValue(True, t.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
checkValue(False, t.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddef"]))
checkValue(True, t.arrayStringsAreEqual(["a", "d", "f"], ["ad", "f"]))
