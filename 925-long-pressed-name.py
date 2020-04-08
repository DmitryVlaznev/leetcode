# 925. Long Pressed Name

# Your friend is typing his name into a keyboard.  Sometimes, when
# typing a character c, the key might get long pressed, and the
# character will be typed 1 or more times.

# You examine the typed characters of the keyboard.  Return True if it
# is possible that it was your friends name, with some characters
# (possibly none) being long pressed.

# Example 1:
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.

# Example 2:
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

# Example 3:
# Input: name = "leelee", typed = "lleeelee"
# Output: true

# Example 4:
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.

# Note:
# name.length <= 1000
# typed.length <= 1000
# The characters of name and typed are lowercase letters.

from typing import List


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        len_name = len(name)
        len_typed = len(typed)
        p = 0
        q = 0
        while p < len_name:
            nl = name[p]
            nc = 0
            while p < len_name and name[p] == nl:
                nc += 1
                p += 1

            if q == len_typed: return False

            tl = typed[q]
            tc = 0
            while q < len_typed and typed[q] == tl:
                tc += 1
                q += 1

            if tc < nc: return False
        return True

t = Solution()
print("True = ", t.isLongPressedName("alex", "aaleex"))
print("False = ", t.isLongPressedName("saeed", "ssaaedd"))
print("True = ", t.isLongPressedName("leelee", "lleeelee"))
print("True = ", t.isLongPressedName("laiden", "laiden"))
print("False = ", t.isLongPressedName("aaa", "ld"))
print("False = ", t.isLongPressedName("aaa", "aa"))
print("True = ", t.isLongPressedName("aaa", "aaaa"))
print("False = ", t.isLongPressedName("adc", "ad"))
print("True = ", t.isLongPressedName("", ""))