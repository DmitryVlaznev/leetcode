# 316.Remove Duplicate Letters

# Given a string s, remove duplicate letters so that every letter
# appears once and only once. You must make sure your result is the
# smallest in lexicographical order among all possible results.

# Note: This question is the same as 1081:
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"

# Constraints:
# 1 <= s.length <= 104
# s consists of lowercase English letters.

from utils import checkValue

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        selected = set()
        last = {}
        res = []
        for i, letter in enumerate(s): last[letter] = i
        for i, letter in enumerate(s):
            if letter in selected: continue
            while res and res[-1] > letter and last[res[-1]] > i:
                selected.discard(res.pop())
            res.append(letter)
            selected.add(letter)
        return "".join(res)

t = Solution()

checkValue("abc", t.removeDuplicateLetters("bcabc"))
checkValue("acdb", t.removeDuplicateLetters("cbacdcbc"))