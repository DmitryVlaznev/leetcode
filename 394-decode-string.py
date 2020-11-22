# 394. Decode String

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string
# inside the square brackets is being repeated exactly k times. Note
# that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white
# spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain
# any digits and that digits are only for those repeat numbers, k. For
# example, there won't be input like 3a or 2[4].


# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"

# Constraints:
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

from utils import checkValue


class Solution:
    def decodeString(self, s: str) -> str:
        def parse(s: str):
            parts, part, repeat, p = [], [], 0, 0
            while p < len(s):
                if s[p].isalpha():
                    part.append(s[p])
                elif s[p].isnumeric() and p > 0 and not s[p - 1].isnumeric():
                    parts.append("".join(part))
                    part = [s[p]]
                elif s[p].isnumeric() and (p == 0 or s[p - 1].isnumeric()):
                    part.append(s[p])
                elif s[p] == "[":
                    repeat = int("".join(part))
                    q = p + 1
                    skip = 0
                    while s[q] != "]" or skip:
                        if s[q] == "[":
                            skip += 1
                        elif s[q] == "]":
                            skip -= 1
                        q += 1
                    template = parse(s[p + 1 : q])
                    parts.append("".join([template] * repeat))
                    repeat = 0
                    part = []
                    p = q
                p += 1
            parts.append("".join(part))
            return "".join(parts)

        return parse(s)


t = Solution()

checkValue("aaabcbc", t.decodeString("3[a]2[bc]"))
checkValue("accaccacc", t.decodeString("3[a2[c]]"))
checkValue("abcabccdcdcdef", t.decodeString("2[abc]3[cd]ef"))
checkValue("abccdcdcdxyz", t.decodeString("abc3[cd]xyz"))
checkValue("abc", t.decodeString("abc"))
checkValue("a", t.decodeString("a"))
checkValue("aaa", t.decodeString("3[a]"))
checkValue("aaabbb", t.decodeString("3[a]bbb"))
checkValue(
    "acwlrlrlrcwlrlrlracwlrlrlrcwlrlrlracwlrlrlrcwlrlrlr",
    t.decodeString("3[a2[cw3[lr]]]"),
)
