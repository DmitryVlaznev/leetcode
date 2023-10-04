# 788. Rotated Digits

# Medium

# An integer x is a good if after rotating each digit individually by
# 180 degrees, we get a valid number that is different from x. Each
# digit must be rotated - we cannot choose to leave it alone.

# A number is valid if each digit remains a digit after rotation. For
# example:

# 0, 1, and 8 rotate to themselves,
# 2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
# 6 and 9 rotate to each other, and
# the rest of the numbers do not rotate to any other number and become invalid.
# Given an integer n, return the number of good integers in the range [1, n].

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

# Example 2:
# Input: n = 1
# Output: 0

# Example 3:
# Input: n = 2
# Output: 1

# Constraints:
# 1 <= n <= 10^4


class Solution:
    def rotatedDigits(self, n: int) -> int:
        prohibited = set([3, 4, 7])
        must_be = set([2, 5, 6, 9])
        res = 0
        for i in range(n + 1):
            d, p, m = 1000, False, False
            while i > 0:
                t = i // d
                p, m = p or t in prohibited, m or t in must_be
                i -= t * d
                d = d // 10
            if m and not p:
                res += 1
        return res


from utils import checkValue

s = Solution()
checkValue(4, s.rotatedDigits(10))
checkValue(0, s.rotatedDigits(1))
checkValue(1, s.rotatedDigits(2))
checkValue(247, s.rotatedDigits(857))
