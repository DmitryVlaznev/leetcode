# 633. Sum of Square Numbers

# Medium

# Given a non-negative integer c, decide whether there're two integers a
# and b such that a^2 + b^2 = c.

# Example 1:
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5

# Example 2:
# Input: c = 3
# Output: false

# Example 3:
# Input: c = 4
# Output: true

# Example 4:
# Input: c = 2
# Output: true

# Example 5:
# Input: c = 1
# Output: true

# Constraints:
# 0 <= c <= 2^31 - 1

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        squares = []
        n = 1
        while True:
            s = n ** 2
            if s > c:
                break
            squares.append(s)
            n += 1
        if c in squares:
            return True
        l, r = 0, len(squares) - 1
        while l <= r:
            pair_sum = squares[l] + squares[r]
            if pair_sum == c:
                return True
            elif pair_sum > c:
                r -= 1
            elif pair_sum < c:
                l += 1
        return False