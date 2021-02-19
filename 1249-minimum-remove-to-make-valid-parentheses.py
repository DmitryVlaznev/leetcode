# 1249. Minimum Remove to Make Valid Parentheses

# Medium

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')',
# in any positions ) so that the resulting parentheses string is valid
# and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are
# valid strings, or
# It can be written as (A), where A is a valid string.

# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Example 2:
# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.

# Example 4:
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"

# Constraints:
# 1 <= s.length <= 10^5
# s[i] is one of  '(' , ')' and lowercase English letters.


from utils import checkValue


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        woRights, parentheses = [], []
        for l in s:
            if l != "(" and l != ")":
                woRights.append(l)
            elif l == "(":
                parentheses.append("(")
                woRights.append(l)
            elif parentheses and parentheses[-1] == "(":
                parentheses.pop()
                woRights.append(l)
        woLefts = []
        for l in reversed(woRights):
            if l != "(" and l != ")":
                woLefts.append(l)
            elif l == ")":
                parentheses.append(")")
                woLefts.append(l)
            elif parentheses and parentheses[-1] == ")":
                parentheses.pop()
                woLefts.append(l)
        return "".join(reversed(woLefts))


t = Solution()

checkValue("lee(t(c)o)de", t.minRemoveToMakeValid("lee(t(c)o)de)"))
checkValue("lee(t(c)o)de", t.minRemoveToMakeValid("lee(t(c)o)(de"))
checkValue("ab(c)d", t.minRemoveToMakeValid("a)b(c)d"))
checkValue("", t.minRemoveToMakeValid("))(("))
checkValue("a(b(c)d)", t.minRemoveToMakeValid("(a(b(c)d)"))
checkValue("", t.minRemoveToMakeValid("("))
checkValue("", t.minRemoveToMakeValid(")"))
checkValue("e", t.minRemoveToMakeValid("e"))