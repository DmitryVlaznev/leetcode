# 1657. Determine if Two Strings Are Close

# Medium

# Two strings are considered close if you can attain one from the other
# using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb

# Operation 2: Transform every occurrence of one existing character into
# another existing character, and do the same with the other character.

# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn
# into a's)
# You can use the operations on either string as many times as necessary.
# Given two strings, word1 and word2, return true if word1 and word2 are
# close, and false otherwise.

# Example 1:
# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"

# Example 2:
# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice
# versa, in any number of operations.

# Example 3:
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"

# Example 4:
# Input: word1 = "cabbba", word2 = "aabbss"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice
# versa, in any amount of operations.


# Constraints:

# 1 <= word1.length, word2.length <= 105
# word1 and word2 contain only lowercase English letters.

from utils import checkValue


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter

        c1 = Counter(word1)
        keys1 = set(c1.keys())
        values1 = list(c1.values())
        values1.sort()

        c2 = Counter(word2)
        keys2 = set(c2.keys())
        values2 = list(c2.values())
        values2.sort()

        return keys1 == keys2 and values1 == values2


t = Solution()
checkValue(True, t.closeStrings("abc", "bca"))
checkValue(False, t.closeStrings("a", "aa"))
checkValue(True, t.closeStrings("cabbba", "abbccc"))
checkValue(False, t.closeStrings("cabbba", "aabbss"))
checkValue(False, t.closeStrings("aabb", "aass"))