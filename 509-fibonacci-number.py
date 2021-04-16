# 509. Fibonacci Number

# Easy

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called
# the Fibonacci sequence, such that each number is the sum of the two
# preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

# Constraints:
# 0 <= n <= 30

from utils import checkValue


class Solution:
    def fib(self, n: int) -> int:
        f, last = [0, 1], 1
        if n < 2:
            return f[n]
        while last < n:
            nxt = f[0] + f[1]
            f[0], f[1], last = f[1], nxt, last + 1
        return f[1]


t = Solution()

checkValue(0, t.fib(0))
checkValue(1, t.fib(1))
checkValue(1, t.fib(2))
checkValue(2, t.fib(3))
checkValue(3, t.fib(4))