# 415. Add Strings

# Easy

# Given two non-negative integers, num1 and num2 represented as string,
# return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for
# handling large integers (such as BigInteger). You must also not
# convert the inputs to integers directly.


# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"

# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"

# Constraints:
# 1 <= num1.length, num2.length <= 10^4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.


from utils import checkValue


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        a = num1 if len(num1) > len(num2) else num2
        b = num2 if a == num1 else num1

        p, q, memo = len(a) - 1, len(b) - 1, 0
        res = []
        while p >= 0:
            s1, s2 = int(a[p]), int(b[q]) if q >= 0 else 0

            res.append((s1 + s2 + memo) % 10)
            memo = (s1 + s2 + memo) // 10
            p, q = p - 1, q - 1
        if memo:
            res.append(memo)
        return "".join([str(d) for d in reversed(res)])


s = Solution()

checkValue("134", s.addStrings("11", "123"))
checkValue("533", s.addStrings("456", "77"))
checkValue("0", s.addStrings("0", "0"))
checkValue("116", s.addStrings("17", "99"))
checkValue("10", s.addStrings("7", "3"))