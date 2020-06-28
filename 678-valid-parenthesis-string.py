# 678. Valid Parenthesis String

# Given a string containing only three types of characters: '(', ')' and
# '*', write a function to check whether this string is valid. We define
# the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single
# left parenthesis '(' or an empty string.
# An empty string is also valid.

# Example 1:
# Input: "()"
# Output: True

# Example 2:
# Input: "(*)"
# Output: True

# Example 3:
# Input: "(*))"
# Output: True

# Note:
# The string size will be in the range [1, 100].

class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        asterisk = []
        for i, letter in enumerate(s):
            if letter == "(": left.append(i)
            elif letter == "*": asterisk.append(i)
            elif letter == ")" and left: left.pop()
            elif letter == ")" and asterisk: asterisk.pop()
            else: return False

        while left and asterisk:
            if left.pop() > asterisk.pop(): return False

        return len(left) == 0

t = Solution()
print("True = ", t.checkValidString(""))
print("True = ", t.checkValidString("***"))
print("True = ", t.checkValidString("()"))
print("True = ", t.checkValidString("(*)"))
print("True = ", t.checkValidString("(*)"))
print("True = ", t.checkValidString("(*))"))
print("True = ", t.checkValidString("((***)"))
print("True = ", t.checkValidString("((*)"))
print("True = ", t.checkValidString("((*))"))
print("True = ", t.checkValidString("()()(**())"))
print("True = ", t.checkValidString("((*(*))"))
print("True = ", t.checkValidString("()**"))

print("False = ", t.checkValidString("()*))"))
print("False = ", t.checkValidString("(*)))"))
print("False = ", t.checkValidString("**()*())))))"))
print("False = ", t.checkValidString(")**"))
print("False = ", t.checkValidString("**("))