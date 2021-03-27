# 869. Reordered Power of 2

# Medium

# Starting with a positive integer N, we reorder the digits in any order
# (including the original order) such that the leading digit is not
# zero.

# Return true if and only if we can do this in a way such that the
# resulting number is a power of 2.

# Example 1:
# Input: 1
# Output: true

# Example 2:
# Input: 10
# Output: false

# Example 3:
# Input: 16
# Output: true

# Example 4:
# Input: 24
# Output: false

# Example 5:
# Input: 46
# Output: true

# Note:
# 1 <= N <= 10^9

from collections import Counter
from utils import checkValue


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        c1 = Counter(str(N))
        for i in range(0, 31):
            c2 = Counter(str(1 << i))
            if c1 == c2:
                return True
        return False


t = Solution()

checkValue(True, t.reorderedPowerOf2(1))
checkValue(True, t.reorderedPowerOf2(16))
checkValue(True, t.reorderedPowerOf2(46))
checkValue(False, t.reorderedPowerOf2(137))
checkValue(False, t.reorderedPowerOf2(10))
checkValue(False, t.reorderedPowerOf2(24))