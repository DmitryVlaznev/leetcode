# 326. Power of Three

# Easy

# Given an integer n, return true if it is a power of three. Otherwise,
# return false.

# An integer n is a power of three, if there exists an integer x such
# that n == 3^x.


# Example 1:
# Input: n = 27
# Output: true

# Example 2:
# Input: n = 0
# Output: false

# Example 3:
# Input: n = 9
# Output: true

# Example 4:
# Input: n = 45
# Output: false

# Constraints:
# -2^31 <= n <= 2^31 - 1

# Follow up: Could you solve it without loops/recursion?

from utils import checkValue


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        l, r = -1, 19
        while r - l > 1:
            mid = l + (r - l) // 2
            if 3 ** mid < n:
                l = mid
            else:
                r = mid

        return 3 ** r == n


t = Solution()

checkValue(True, t.isPowerOfThree(27))
checkValue(False, t.isPowerOfThree(42))
checkValue(True, t.isPowerOfThree(9))
