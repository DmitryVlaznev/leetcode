# 772. Basic Calculator III

# Hard

# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, /
# operators , open ( and closing parentheses ) and empty spaces . The
# integer division should truncate toward zero.

# You may assume that the given expression is always valid. All
# intermediate results will be in the range of [-2147483648,
# 2147483647].

# Follow up: Could you solve the problem without using built-in library
# functions.


# Example 1:
# Input: s = "1 + 1"
# Output: 2

# Example 2:
# Input: s = " 6-4 / 2 "
# Output: 4

# Example 3:
# Input: s = "2*(5+5*2)/3+(6/2+8)"
# Output: 21

# Example 4:
# Input: s = "(2+6* 3+5- (3*14/7+2)*5)+3"
# Output: -12

# Example 5:
# Input: s = "0"
# Output: 0

# Constraints:
# 1 <= s <= 104
# s consists of digits, '+', '-', '*', '/', '(', ')' and ' '.
# s is a valid expression.

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

        def process_mul_div(stack):
            if len(stack) >= 3 and stack[-2] in ["*", "/"]:
                b = stack.pop()
                op = stack.pop()
                a = stack.pop()
                if op == "*":
                    stack.append(int(a * b))
                else:
                    stack.append(int(a / b))

        stack, p, acc, last_multiplier = [], 0, None, 1
        while p < len(cleared):
            c = cleared[p]
            if c == "+" or c == "-":
                if acc is not None:
                    stack.append(int(acc) * last_multiplier)
                process_mul_div(stack)
                last_multiplier = -1 if c == "-" else 1
                acc = None
            elif c.isdigit():
                acc = acc + c if acc is not None else c
            elif c == "(":
                stack.append(last_multiplier)
                stack.append("(")
                last_multiplier = 1
            elif c == ")":
                if acc is not None:
                    stack.append(int(acc) * last_multiplier)
                process_mul_div(stack)
                acc = 0
                while stack[-1] != "(":
                    acc += stack.pop()
                stack.pop()
                acc *= stack.pop()
                stack.append(acc)
                acc = None
                process_mul_div(stack)
            elif c == "*" or c == "/":
                if acc is not None:
                    stack.append(int(acc) * last_multiplier)
                process_mul_div(stack)

                stack.append(c)
                last_multiplier = 1
                acc = None
            p += 1
        if acc:
            stack.append(int(acc) * last_multiplier)
            process_mul_div(stack)
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

checkValue(7, t.calculate("3+2*2"))
checkValue(7, t.calculate(" 3  + 2* 2 "))
checkValue(1, t.calculate(" 3/2 "))
checkValue(5, t.calculate(" 3+5 / 2 "))
checkValue(2, t.calculate(" 30 /3/5 "))
checkValue(1, t.calculate("1-1+1"))
checkValue(10, t.calculate("4*5/2"))

checkValue(21, t.calculate("2*(5+5*2)/3+(6/2+8)"))
checkValue(-12, t.calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))
checkValue(0, t.calculate("0"))