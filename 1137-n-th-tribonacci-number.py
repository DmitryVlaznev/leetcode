# 1137. N-th Tribonacci Number

# Easy

# The Tribonacci sequence Tn is defined as follows:

# T(0) = 0, T(1) = 1, T(2) = 1, and T(n+3) = T(n) + T(n+1) + T(n+2) for n >= 0.

# Given n, return the value of Tn.


# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
# Input: n = 25
# Output: 1389537

# Constraints:

# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return ([0, 1, 1])[n]
        t3, t2, t1 = 0, 1, 1
        for _ in range(3, n + 1):
            t3, t2, t1 = t2, t1, t1 + t2 + t3
        return t1