# 1663. Smallest String With A Given Numeric Value

# Medium

# The numeric value of a lowercase character is defined as its position
# (1-indexed) in the alphabet, so the numeric value of a is 1, the
# numeric value of b is 2, the numeric value of c is 3, and so on.

# The numeric value of a string consisting of lowercase characters is
# defined as the sum of its characters' numeric values. For example, the
# numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

# You are given two integers n and k. Return the lexicographically
# smallest string with length equal to n and numeric value equal to k.

# Note that a string x is lexicographically smaller than string y if x
# comes before y in dictionary order, that is, either x is a prefix of
# y, or if i is the first position such that x[i] != y[i], then x[i]
# comes before y[i] in alphabetic order.

# Example 1:
# Input: n = 3, k = 27
# Output: "aay"
# Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and
# it is the smallest string with such a value and length equal to 3.

# Example 2:
# Input: n = 5, k = 73
# Output: "aaszz"

# Constraints:
# 1 <= n <= 10^5
# n <= k <= 26 * n

from utils import checkValue


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = []
        while n:
            if k - n >= 26:
                mul = (k - n) // 26
                res += ["z"] * mul
                k, n = k - 26 * mul, n - mul
            elif k - n > 0:
                l = chr(ord("a") + k - n)
                res.append(l)
                k = n = n - 1
            else:
                res += ["a"] * n
                k = n = 0
        res.reverse()
        return "".join(res)


t = Solution()

checkValue("aaszz", t.getSmallestString(5, 73))
checkValue("aay", t.getSmallestString(3, 27))
checkValue("bz", t.getSmallestString(2, 28))
checkValue("az", t.getSmallestString(2, 27))
checkValue("f", t.getSmallestString(1, 6))
checkValue("ae", t.getSmallestString(2, 6))
checkValue("a", t.getSmallestString(1, 1))
