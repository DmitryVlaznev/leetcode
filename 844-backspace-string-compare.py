# Backspace String Compare

# Given two strings S and T, return if they are equal when both are
# typed into empty text editors. # means a backspace character.

# Example 1:
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".

# Example 2:
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".

# Example 3:
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".

# Example 4:
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

# Note:
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:

# Can you solve it in O(N) time and O(1) space?

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        p = len(S) - 1
        q = len(T) - 1
        bs = bt = 0
        while p >= 0 or q >= 0:
            next_s = S[p] if p >= 0 else ""
            while p >= 0 and (next_s == "#" or bs > 0):
                bs = bs + 1 if next_s == "#" else bs - 1
                p -= 1
                next_s = S[p] if p >= 0 else ""

            next_t = T[q] if q >= 0 else ""
            while q >= 0 and (next_t == "#" or bt > 0):
                bt = bt + 1 if next_t == "#" else bt - 1
                q -= 1
                next_t = T[q] if q >= 0 else ""

            if next_s != next_t: return False
            p -= 1
            q -= 1
        return True


t = Solution()
print("True = ", t.backspaceCompare("ab#c", "ad#c"))
print("True = ", t.backspaceCompare("ab#c", "a345#6###c"))
print("True = ", t.backspaceCompare("ab##", "c#d#"))
print("True = ", t.backspaceCompare("a##c", "#a#c"))
print("False = ", t.backspaceCompare("a#c", "b"))
print("True = ", t.backspaceCompare("#c", "###c"))
print("True = ", t.backspaceCompare("", "###"))
print("True = ", t.backspaceCompare("", ""))
print("True = ", t.backspaceCompare("xywrrmp", "xywrrmu#p"))
print("False = ", t.backspaceCompare("bxj##tw", "bxj###tw"))
print("False = ", t.backspaceCompare("bbbextm", "bbb#extm"))


