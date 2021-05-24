# 709. To Lower Case

# Easy

# Given a string s, return the string after replacing every uppercase
# letter with the same lowercase letter.

# Example 1:
# Input: s = "Hello"
# Output: "hello"

# Example 2:
# Input: s = "here"
# Output: "here"

# Example 3:
# Input: s = "LOVELY"
# Output: "lovely"

# Constraints:
# 1 <= s.length <= 100
# s consists of printable ASCII characters.


class Solution:
    def toLowerCase(self, s: str) -> str:
        res, start, end, diff = [], ord("A"), ord("Z"), ord("A") - ord("a")
        for l in s:
            lc = ord(l)
            if lc >= start and lc <= end:
                l = chr(lc - diff)
            res.append(l)
        return "".join(res)