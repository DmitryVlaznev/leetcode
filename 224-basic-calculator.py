# 224. Basic Calculator

# Hard

# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .

# Example 1:
# Input: "1 + 1"
# Output: 2

# Example 2:
# Input: " 2-1 + 2 "
# Output: 3

# Example 3:
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23

# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

from utils import checkValue


class Solution:
    def calculate(self, s: str) -> int:
        p, cleared = 0, []
        while p < len(s):
            if s[p] != " ":
                cleared.append(s[p])
            p += 1
        if not cleared:
            return 0

        stack, p, acc, last_multiplier = [], 0, None, 1
        while p < len(cleared):
            c = cleared[p]
            if c == "+" or c == "-":
                if acc is not None:
                    stack.append(int(acc) * last_multiplier)
                last_multiplier = -1 if c == "-" else 1
                acc = None
            elif c.isdigit():
                acc = acc + c if acc is not None else c
            elif c == "(":
                stack.append(last_multiplier)
                stack.append("(")
                last_multiplier = 1
            elif c == ")":
                acc = int(acc) * last_multiplier if acc is not None else 0
                while stack[-1] != "(":
                    acc += stack.pop()
                stack.pop()
                acc *= stack.pop()
                stack.append(acc)
                acc = None
            p += 1
        if acc:
            stack.append(int(acc) * last_multiplier)
        return sum(stack)


t = Solution()
checkValue(2, t.calculate("1 + 1"))
checkValue(3, t.calculate(" 2-1 + 2 "))
checkValue(23, t.calculate("(1+(4+5+2)-3)+(6+8)"))
checkValue(5, t.calculate("1+(5+2)-3"))
checkValue(5, t.calculate(" 1  +(   5 +    2 ) -3"))
checkValue(-4, t.calculate("(1+2)-(5+2)"))
checkValue(3, t.calculate("    3  "))
checkValue(34, t.calculate("    34  "))
checkValue(3, t.calculate("   (  3 ) "))
checkValue(34, t.calculate("   (  34 ) "))
checkValue(22, t.calculate("23 - (8-(5+ 2))"))
checkValue(18, t.calculate("23 - ((8-5) +2)"))