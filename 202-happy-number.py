# 202. Happy Number

# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting
# with any positive integer, replace the number by the sum of the
# squares of its digits, and repeat the process until the number equals
# 1 (where it will stay), or it loops endlessly in a cycle which does
# not include 1. Those numbers for which this process ends in 1 are
# happy numbers.

# Example:
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

from typing import List


class Solution:
    def getNext(self, n: int) -> int:
        squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        digits = []
        factor = 1
        while n:
            next_factor = factor * 10
            part = n % next_factor
            digit = part // factor
            n -= part
            digits.append(digit)
            factor = next_factor
        res = 0
        for digit in digits:
            res += squares[digit]
        return res

    def isHappy(self, n: int) -> bool:
        checked = {}
        while True:
            if n in checked: return False
            if n ==1: return True

            checked[n] = True
            n = self.getNext(n)

test = Solution()

print("[10 True] => ", test.isHappy(10))
print("[19 True] => ", test.isHappy(19))
print("[1942 False] => ", test.isHappy(1942))
print("[0 False] => ", test.isHappy(0))