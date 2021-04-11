# 953. Verifying an Alien Dictionary

# Easy

# In an alien language, surprisingly they also use english lowercase
# letters, but possibly in a different order. The order of the alphabet
# is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order
# of the alphabet, return true if and only if the given words are sorted
# lexicographicaly in this alien language.

# Example 1:
# Input: words = ["hello","leetcode"], order =
# "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the
# sequence is sorted.

# Example 2:
# Input: words = ["word","world","row"], order =
# "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] >
# words[1], hence the sequence is unsorted.

# Example 3:
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second
# string is shorter (in size.) According to lexicographical rules
# "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank
# character which is less than any other character (More info).

# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.

from typing import List
from utils import checkValue


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indices = {l: i for i, l in enumerate(order)}
        for i in range(len(words) - 1):
            word1, word2, p1, p2, equal = words[i], words[i + 1], 0, 0, True
            while p1 < len(word1) and p2 < len(word2):
                if indices[word1[p1]] == indices[word2[p2]]:
                    p1, p2 = p1 + 1, p2 + 1
                    continue
                elif indices[word1[p1]] < indices[word2[p2]]:
                    equal = False
                    break
                else:
                    return False
            if equal and len(word1) > len(word2):
                return False
        return True


t = Solution()

checkValue(True, t.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
checkValue(
    False, t.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz")
)
checkValue(False, t.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))
checkValue(True, t.isAlienSorted(["apple"], "abcdefghijklmnopqrstuvwxyz"))
checkValue(True, t.isAlienSorted(["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz"))
