# 12. Integer to Roman

# Medium

# Roman numerals are represented by seven different symbols: I, V, X, L,
# C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27
# is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to
# right. However, the numeral for four is not IIII. Instead, the number
# four is written as IV. Because the one is before the five we subtract
# it making four. The same principle applies to the number nine, which
# is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.

# Example 1:
# Input: num = 3
# Output: "III"

# Example 2:
# Input: num = 4
# Output: "IV"

# Example 3:
# Input: num = 9
# Output: "IX"

# Example 4:
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 5:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:
# 1 <= num <= 3999

from utils import checkValue


class Solution:
    def intToRoman(self, num: int) -> str:
        letters = [
            {1: "M"},
            {1: "C", 5: "D"},
            {1: "X", 5: "L"},
            {1: "I", 5: "V"},
        ]
        mul = [1000, 100, 10, 1]
        res = []
        i = 0
        while i < 4:
            d = num // mul[i]
            num -= d * mul[i]

            if d == 9:
                res.append(letters[i][1] + letters[i - 1][1])
            elif d == 4:
                res.append(letters[i][1] + letters[i][5])
            else:
                if d // 5:
                    res.append(letters[i][5])
                    d -= 5
                while d:
                    res.append(letters[i][1])
                    d -= 1
            i += 1
        return "".join(res)


t = Solution()

checkValue("I", t.intToRoman(1))
checkValue("II", t.intToRoman(2))
checkValue("IV", t.intToRoman(4))
checkValue("VII", t.intToRoman(7))
checkValue("IX", t.intToRoman(9))

checkValue("X", t.intToRoman(10))
checkValue("XI", t.intToRoman(11))
checkValue("XIV", t.intToRoman(14))
checkValue("XV", t.intToRoman(15))
checkValue("XVIII", t.intToRoman(18))
checkValue("XIX", t.intToRoman(19))

checkValue("MMMCMXCIX", t.intToRoman(3999))
checkValue("MMMCMXLV", t.intToRoman(3945))
checkValue("MMMDCCCXLV", t.intToRoman(3845))
