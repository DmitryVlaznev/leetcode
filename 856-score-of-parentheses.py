# 856. Score of Parentheses

# Medium

# Given a balanced parentheses string S, compute the score of the string
# based on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

# Example 1:
# Input: "()"
# Output: 1

# Example 2:
# Input: "(())"
# Output: 2

# Example 3:
# Input: "()()"
# Output: 2

# Example 4:
# Input: "(()(()))"
# Output: 6

# Note:
# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50

from utils import checkValue


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for p in S:
            if p == "(":
                stack.append(p)
            else:
                r = 0
                while stack[-1] != "(":
                    r += stack.pop()
                stack.pop()
                stack.append(max(1, r * 2))
        return sum(stack)


t = Solution()

checkValue(1, t.scoreOfParentheses("()"))
checkValue(2, t.scoreOfParentheses("(())"))
checkValue(2, t.scoreOfParentheses("()()"))
checkValue(6, t.scoreOfParentheses("(()(()))"))
checkValue(10, t.scoreOfParentheses("(()(()()))"))
checkValue(0, t.scoreOfParentheses(""))