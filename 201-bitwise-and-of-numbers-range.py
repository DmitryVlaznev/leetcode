# 201. Bitwise AND of Numbers Range

# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the
# bitwise AND of all numbers in this range, inclusive.

# Example 1:
# Input: [5,7]
# Output: 4

# Example 2:
# Input: [0,1]
# Output: 0

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        c = 0
        while n != m:
            n = n >> 1
            m = m >> 1
            c += 1
        return n << c

    def rangeBitwiseAndBrute(self, m: int, n: int) -> int:
        res = 2147483647
        for i in range(m, n + 1):
            res = res & i
        return res

    def rangeBitwiseAndFirstApproach(self, m: int, n: int) -> int:
        res = 0
        diff = n - m
        for bit in range(31, -1, -1):
            max_diff = 2 ** bit - 1
            if (diff > max_diff): break

            mask = 1 << bit
            res = res | (m & n & mask)
        return res

t = Solution()
print(t.rangeBitwiseAnd(3, 4), " = ", t.rangeBitwiseAndBrute(3, 4), " = ", t.rangeBitwiseAndFirstApproach(3, 4), " # ", 3 & 4)
print(t.rangeBitwiseAnd(4, 7), " = ", t.rangeBitwiseAndBrute(4, 7), " = ", t.rangeBitwiseAndFirstApproach(4, 7), " # ", 4 & 7)
print(t.rangeBitwiseAnd(2, 3), " = ", t.rangeBitwiseAndBrute(2, 3), " = ", t.rangeBitwiseAndFirstApproach(2, 3), " # ", 2 & 3)
print(t.rangeBitwiseAnd(42, 42), " = ", t.rangeBitwiseAndBrute(42, 42), " = ", t.rangeBitwiseAndFirstApproach(42, 42), " # ", 42 & 42)
print(t.rangeBitwiseAnd(0, 123435), " = ", t.rangeBitwiseAndBrute(0, 123435), " = ", t.rangeBitwiseAndFirstApproach(0, 123435), " # ", 0 & 123435)
print(t.rangeBitwiseAnd(5, 7), " = ", t.rangeBitwiseAndBrute(5, 7), " = ", t.rangeBitwiseAndFirstApproach(5, 7), " # ", 5 & 7)
print(t.rangeBitwiseAnd(55674389, 55678976), " = ", t.rangeBitwiseAndBrute(55674389, 55678976), " = ", t.rangeBitwiseAndFirstApproach(55674389, 55678976), " # ", 55674389 & 55678976)