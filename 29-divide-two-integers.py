# 29. Divide Two Integers

# Medium

# Given two integers dividend and divisor, divide two integers without
# using multiplication, division, and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero, which means losing
# its fractional part. For example, truncate(8.345) = 8 and
# truncate(-2.7335) = -2.

# Note:

# Assume we are dealing with an environment that could only store
# integers within the 32-bit signed integer range: [−231,  231 − 1]. For
# this problem, assume that your function returns 231 − 1 when the
# division result overflows.

# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.

# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.

# Example 3:
# Input: dividend = 0, divisor = 1
# Output: 0

# Example 4:
# Input: dividend = 1, divisor = 1
# Output: 1

# Constraints:
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0

from utils import checkValue


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        positive = (dividend < 0) == (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        powers = [(1, b)]
        while powers[-1][1] << 1 <= a:
            powers.append((powers[-1][0] << 1, powers[-1][1] << 1))

        res = 0
        for power, subtrahend in reversed(powers):
            if subtrahend <= a:
                res, a = res + power, a - subtrahend
        return res if positive else -res


t = Solution()

checkValue(14, t.divide(100, 7))
checkValue(8, t.divide(56, 7))
checkValue(0, t.divide(0, 42))
checkValue(0, t.divide(0, -42))
checkValue(3, t.divide(10, 3))
checkValue(-2, t.divide(7, -3))
checkValue(-2, t.divide(-7, 3))
checkValue(2, t.divide(-7, -3))
checkValue(1, t.divide(1, 1))
checkValue(3, t.divide(9, 3))
checkValue(-1, t.divide(-37, 30))
checkValue(1, t.divide(37, 30))
checkValue(2147483647, t.divide(-2147483648, -1))