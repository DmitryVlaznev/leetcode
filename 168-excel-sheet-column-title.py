# 168. Excel Sheet Column Title

# Easy

# Given an integer columnNumber, return its corresponding column title
# as it appears in an Excel sheet.

# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...


# Example 1:
# Input: columnNumber = 1
# Output: "A"

# Example 2:
# Input: columnNumber = 28
# Output: "AB"

# Example 3:
# Input: columnNumber = 701
# Output: "ZY"


# Constraints:
# 1 <= columnNumber <= 2^31 - 1

from utils import checkValue


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res, n = [], columnNumber
        while n:
            n -= 1
            digit = n % 26
            res.append(chr(ord("A") + digit))
            n = n // 26

        res.reverse()
        return "".join(res)


s = Solution()
checkValue("A", s.convertToTitle(1))
checkValue("Z", s.convertToTitle(26))
checkValue("AA", s.convertToTitle(27))
checkValue("AY", s.convertToTitle(51))
checkValue("AZ", s.convertToTitle(52))
checkValue("ZY", s.convertToTitle(701))