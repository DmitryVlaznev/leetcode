# 1119. Remove Vowels from a String

# Easy

# Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from
# it, and return the new string.

# Example 1:
# Input: s = "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"

# Example 2:
# Input: s = "aeiou"
# Output: ""


# Constraints:
# 1 <= s.length <= 1000
# s consists of only lowercase English letters.


class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u"])
        res = []
        for l in s:
            if l not in vowels:
                res.append(l)
        return "".join(res)
