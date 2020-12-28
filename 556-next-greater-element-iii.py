# 556. Next Greater Element III

# Medium

# Given a positive integer n, find the smallest integer which has
# exactly the same digits existing in the integer n and is greater in
# value than n. If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, if there
# is a valid answer but it does not fit in 32-bit integer, return -1.

# Example 1:
# Input: n = 12
# Output: 21

# Example 2:
# Input: n = 21
# Output: -1

# Constraints:
# 1 <= n <= 2^31 - 1

from utils import checkValue


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = [d for d in str(n)]
        p = len(digits) - 2
        while p > -1 and digits[p] >= digits[p + 1]:
            p -= 1
        if p == -1:
            return -1
        q = p + 1
        while q < len(digits) - 1 and digits[q + 1] > digits[p]:
            q += 1
        digits[q], digits[p] = digits[p], digits[q]
        res = int("".join(digits[0 : p + 1] + list(reversed(digits[p + 1 :]))))
        return res if res < 2 ** 31 else -1


t = Solution()
checkValue(302, t.nextGreaterElement(230))
checkValue(21, t.nextGreaterElement(12))
checkValue(-1, t.nextGreaterElement(21))
checkValue(-1, t.nextGreaterElement(22))
checkValue(-1, t.nextGreaterElement(1999999999))