# 343. Integer Break

# Medium

# Given an integer n, break it into the sum of k positive integers,
# where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.

# Example 2:
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

# Constraints:
# 2 <= n <= 58

from functools import lru_cache


class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dp(k):
            res = k
            for i in range(1, k):
                res = max(res, i * dp(k - i))
            return res

        res = 0
        for i in range(1, n):
            res = max(res, i * dp(n - i))
        return res


s = Solution()
s.integerBreak(10)