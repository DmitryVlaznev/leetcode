# 227. Basic Calculator II

# Medium

# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces . The integer division should truncate
# toward zero.

# Example 1:
# Input: "3+2*2"
# Output: 7

# Example 2:
# Input: " 3/2 "
# Output: 1

# Example 3:
# Input: " 3+5 / 2 "
# Output: 5

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
        p, parsed, operand, operations = 0, [], [], ["+", "-", "*", "/"]
        while p < len(cleared):
            if cleared[p] in operations:
                parsed.append(int("".join(operand)))
                parsed.append(cleared[p])
                operand = []
            else:
                operand.append(cleared[p])
            p += 1
        parsed.append(int("".join(operand)))

        p, acc, ops = 0, [], []
        while p < len(parsed):
            if parsed[p] in operations:
                ops.append(parsed[p])
            else:
                acc.append(parsed[p])

                if ops and ops[-1] == "*":
                    ops.pop()
                    b = acc.pop()
                    a = acc.pop()
                    acc.append(a * b)
                elif ops and ops[-1] == "/":
                    ops.pop()
                    b = acc.pop()
                    a = acc.pop()
                    acc.append(a // b)
            p += 1
        if not ops:
            return acc[0]

        p, res = 1, acc[0]
        while p < len(acc):
            if ops[p - 1] == "+":
                res += acc[p]
            else:
                res -= acc[p]
            p += 1
        return res


t = Solution()

checkValue(7, t.calculate("3+2*2"))
checkValue(7, t.calculate(" 3  + 2* 2 "))
checkValue(1, t.calculate(" 3/2 "))
checkValue(5, t.calculate(" 3+5 / 2 "))
checkValue(2, t.calculate(" 30 /3/5 "))
checkValue(1, t.calculate("1-1+1"))
checkValue(10, t.calculate("4*5/2"))