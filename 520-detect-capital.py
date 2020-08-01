# 520. Detect Capital

# Given a word, you need to judge whether the usage of capitals in it is
# right or not.

# We define the usage of capitals in a word to be right when one of the
# following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

# Example 1:
# Input: "USA"
# Output: True

# Example 2:
# Input: "FlaG"
# Output: False

# Note: The input will be a non-empty word consisting of uppercase and
# lowercase latin letters.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2: return True
        state = "regular"
        if ord(word[0]) >= ord("A") and ord(word[0]) <= ord("Z"):
            state = "capitalized"
            if len(word) >= 2 and ord(word[1]) >= ord("A") and ord(word[1]) <= ord("Z"):
                state = "abbreviation"

        for i in range(1, len(word)):
            if ord(word[i]) >= ord("A") and ord(word[i]) <= ord("Z"):
                if state != "abbreviation": return False
            else:
                if state == "abbreviation": return False
        return True

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log(True, t.detectCapitalUse(""))
log(True, t.detectCapitalUse("U"))
log(True, t.detectCapitalUse("t"))
log(True, t.detectCapitalUse("TT"))
log(True, t.detectCapitalUse("Tt"))
log(False, t.detectCapitalUse("dR"))
log(False, t.detectCapitalUse("RRRTEYhT"))
log(False, t.detectCapitalUse("RRRTEYh"))
log(False, t.detectCapitalUse("RdsffdgfT"))
log(False, t.detectCapitalUse("RdsfGfdgf"))
log(True, t.detectCapitalUse("dsffdgf"))
log(False, t.detectCapitalUse("dsffTdgf"))