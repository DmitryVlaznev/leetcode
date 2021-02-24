# 524. Longest Word in Dictionary through Deleting

# Medium

# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the
# longest word with the smallest lexicographical order. If there is no
# possible result, return the empty string.

# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# Output:
# "apple"

# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
# Output:
# "a"

# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.

from typing import List
from utils import checkValue


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ""
        for word in d:
            if len(word) < len(res):
                continue

            p = q = 0
            while p < len(s) and q < len(word):
                if word[q] == s[p]:
                    q += 1
                p += 1
            if q == len(word):
                if len(word) == len(res):
                    res = res if res < word else word
                else:
                    res = res if len(res) > len(word) else word
        return res


t = Solution()

checkValue("apple", t.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
checkValue("a", t.findLongestWord("abpcplea", ["a", "b", "c"]))
checkValue("ab", t.findLongestWord("bab", ["ba", "ab", "a", "b"]))
