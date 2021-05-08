# 906. Super Palindromes

# Hard

# Let's say a positive integer is a super-palindrome if it is a
# palindrome, and it is also the square of a palindrome.

# Given two positive integers left and right represented as strings,
# return the number of super-palindromes integers in the inclusive range
# [left, right].


# Example 1:
# Input: left = "4", right = "1000"
# Output: 4
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.

# Example 2:
# Input: left = "1", right = "2"
# Output: 1

# Constraints:
# 1 <= left.length, right.length <= 18
# left and right consist of only digits.
# left and right cannot have leading zeros.
# left and right represent integers in the range [1, 10^18].
# left is less than or equal to right.

import math


class Solution:
    # TLE
    # def superpalindromesInRange(self, left: str, right: str) -> int:
    #     l, r = math.ceil(math.sqrt(int(left))), math.floor(math.sqrt(int(right)))
    #     isPalindrome = lambda s: s == s[::-1]

    #     res = 0
    #     for n in range(l, r + 1):
    #         res += int(isPalindrome(str(n)) and isPalindrome(str(n ** 2)))
    #     return res

    def superpalindromesInRange(self, left: str, right: str) -> int:
        lb, ub = int(left) ** 0.5, int(right) ** 0.5
        sq, ans = ["1", "2"], int(lb <= 3 <= ub)
        isPalindrome = lambda s: s == s[::-1]
        for s in sq:
            if int(s) > ub:
                break
            if int(s) >= lb:
                ans += isPalindrome(str(int(s) ** 2))
            left, odd = divmod(len(s), 2)
            if odd:
                sq += [s[: left + 1] + s[-(left + 1) :]]
            else:
                sq += [s[:left] + d + s[-left:] for d in "012"]
        return ans


t = Solution()

t.superpalindromesInRange(4, 1000)