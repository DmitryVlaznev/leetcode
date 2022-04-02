# 1087. Brace Expansion

# Medium

# You are given a string s representing a list of words. Each letter in
# the word has one or more options.

# If there is one option, the letter is represented as is.
# If there is more than one option, then curly braces delimit the
# options. For example, "{a,b,c}" represents options ["a", "b", "c"].
# For example, if s = "a{b,c}", the first character is always 'a', but
# the second character can be 'b' or 'c'. The original list is ["ab",
# "ac"].
# Return all words that can be formed in this manner, sorted in
# lexicographical order.

# Example 1:
# Input: s = "{a,b}c{d,e}f"
# Output: ["acdf","acef","bcdf","bcef"]

# Example 2:
# Input: s = "abcd"
# Output: ["abcd"]

# Constraints:
# 1 <= s.length <= 50
# s consists of curly brackets '{}', commas ',', and lowercase English
# letters.
# s is guaranteed to be a valid input.
# There are no nested curly brackets.
# All characters inside a pair of consecutive opening and ending curly
# brackets are different.

from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        options = []
        p = 0
        while p < len(s):
            if s[p] != "{":
                options.append([s[p]])
            else:
                q = p + 1
                while s[q] != "}":
                    q += 1
                options.append(list(sorted(s[p + 1 : q].split(","))))
                p = q
            p += 1

        res = []

        def dfs(seq: List["str"], option: int):
            if option == len(options):
                res.append("".join(seq))
                return
            for letter in options[option]:
                seq.append(letter)
                dfs(seq, option + 1)
                seq.pop()

        dfs([], 0)
        return res


s = Solution()

print("{a,b}c{d,e}f", s.expand("{a,b}c{d,e}f"))
print("{a,b}c{e,d}f", s.expand("{a,b}c{e,d}f"))
print("abcd", s.expand("abcd"))
