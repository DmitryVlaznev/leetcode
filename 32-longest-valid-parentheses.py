# 32. Longest Valid Parentheses

# Hard

# Given a string containing just the characters '(' and ')', find the
# length of the longest valid (well-formed) parentheses substring.

# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

# Example 3:
# Input: s = ""
# Output: 0

# Constraints:
# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.

from utils import checkValue


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, res = [-1], 0
        for i, l in enumerate(s):
            if l == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res


t = Solution()

checkValue(2, t.longestValidParentheses("(()"))
checkValue(4, t.longestValidParentheses(")()())"))
checkValue(0, t.longestValidParentheses(""))
checkValue(0, t.longestValidParentheses("("))
checkValue(2, t.longestValidParentheses("()(()"))
checkValue(2, t.longestValidParentheses("(()"))
checkValue(4, t.longestValidParentheses("()()(()"))
checkValue(4, t.longestValidParentheses("(())(()"))
checkValue(6, t.longestValidParentheses("(()(())"))
checkValue(2, t.longestValidParentheses("(()(((()"))