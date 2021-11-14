# 43. Multiply Strings

# Medium

# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the
# inputs to integer directly.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

# Constraints:
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number
# 0 itself.


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def multiply_by_digit(num, digit):
            c, res = 0, []
            for d in reversed(num):
                r = d * digit + c
                res.append(r % 10)
                c = r // 10
            if c:
                res.append(c)
            return list(reversed(res))

        def sum_two(n1, n2):
            l, res, c = max(len(n1), len(n2)), [], 0
            n1.reverse()
            n2.reverse()
            for i in range(l):
                d1, d2 = n1[i] if i < len(n1) else 0, n2[i] if i < len(n2) else 0
                r = d1 + d2 + c
                res.append(r % 10)
                c = r // 10
            if c:
                res.append(c)
            return list(reversed(res))

        s = [int(d) for d in num1] if len(num1) < len(num2) else [int(d) for d in num2]
        l = [int(d) for d in num1] if len(num1) >= len(num2) else [int(d) for d in num2]

        res, s = [], list(reversed(s))
        for i in range(len(s)):
            t = l + [0] * i
            res = sum_two(res, multiply_by_digit(t, s[i]))
        res = "".join([str(d) for d in res])
        return res if int(res) > 0 else "0"