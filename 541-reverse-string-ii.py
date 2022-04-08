# 541. Reverse String II

# Easy

# Given a string s and an integer k, reverse the first k characters for
# every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If
# there are less than 2k but greater than or equal to k characters, then
# reverse the first k characters and leave the other as original.

# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"


# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 10^4


from utils import checkValue


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res, base = [], 0
        while base < len(s):
            start, end = base, min(base + k - 1, len(s) - 1)
            for i in range(end, start - 1, -1):
                res.append(s[i])
            start = end + 1
            end = min(start + k, len(s))
            if start < len(s):
                for i in range(start, end):
                    res.append(s[i])
            base += 2 * k
        return "".join(res)


s = Solution()

checkValue("bacdfeg", s.reverseStr("abcdefg", 2))
checkValue("bacd", s.reverseStr("abcd", 2))