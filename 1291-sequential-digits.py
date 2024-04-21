# 1291. Sequential Digits

# Medium

# An integer has sequential digits if and only if each digit in the
# number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high]
# inclusive that have sequential digits.

# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]

# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]

# Constraints:
# 10 <= low <= high <= 10^9

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        res = []
        for l in range(len(str(low)), len(str(high)) + 1):
            for start in range(0, 10 - l):
                cand = int(digits[start : start + l])
                if cand >= low and cand <= high:
                    res.append(cand)
        return res

    def sequentialDigits2(self, low: int, high: int) -> List[int]:
        def generate_num(length, start):
            res = 0
            for i in range(length):
                res += (10 ** (length - i - 1)) * (start + i)
            return res

        res = []
        low_digits, high_digits = len(str(low)), len(str(high))
        for digits in range(low_digits, high_digits + 1):
            for start in range(1, 10):
                if (start + digits) > 10:
                    break
                n = generate_num(digits, start)
                if n < low:
                    continue
                if n > high:
                    break
                res.append(n)
        return list(sorted(res))


s = Solution()
print(s.sequentialDigits(100, 300))
print(s.sequentialDigits(1000, 13000))
