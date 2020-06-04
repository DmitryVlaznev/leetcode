# 344. Reverse String

# Write a function that reverses a string. The input string is given as
# an array of characters char[].

# Do not allocate extra space for another array, you must do this by
# modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii
# characters.

# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) < 2: return s
        p, q = 0, len(s) - 1
        while p < q:
            s[p], s[q] = s[q], s[p]
            p += 1
            q -= 1

def log(correct, res):
    if len(correct) == len(res) and set(correct) == set(res): print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

s = ["h","e","l","l","o"]
t.reverseString(s)
log(["o","l","l","e","h"], s)

s = ["H","a","n","n","a","h"]
t.reverseString(s)
log(["h","a","n","n","a","H"], s)

s = ["a","n","n"]
t.reverseString(s)
log(["n","n","a"], s)

s = ["a","n"]
t.reverseString(s)
log(["n","a"], s)

s = ["a"]
t.reverseString(s)
log(["a"], s)

s = []
t.reverseString(s)
log([], s)
