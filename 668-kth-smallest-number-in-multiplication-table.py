# 668. Kth Smallest Number in Multiplication Table

# Hard

# Nearly everyone has used the Multiplication Table. The multiplication
# table of size m x n is an integer matrix mat where mat[i][j] == i * j
# (1-indexed).

# Given three integers m, n, and k, return the kth smallest element in
# the m x n multiplication table.


# Example 1:
# Input: m = 3, n = 3, k = 5
# Output: 3
# Explanation: The 5th smallest number is 3.

# Example 2:
# Input: m = 2, n = 3, k = 6
# Output: 6
# Explanation: The 6th smallest number is 6.

# Constraints:
# 1 <= m, n <= 3 * 10^4
# 1 <= k <= m * n


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def less_or_equal(c):
            nonlocal m, n
            res = 0
            for i in range(1, m + 1):
                res += min(n, c // i)
            return res

        l, r = -1, m * n + 1
        while r - l > 1:
            mid = l + (r - l) // 2
            if less_or_equal(mid) >= k:
                r = mid
            else:
                l = mid
        return r