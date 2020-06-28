# 279. Perfect Squares

# Given a positive integer n, find the least number of perfect square
# numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution:

    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i ** 2 <= n:
            squares.append(i ** 2)
            i += 1
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for s in squares:
                if i < s: break
                dp[i] = min(dp[i], dp[i - s] + 1)
        return dp[-1]

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log(3, t.numSquares(12))
log(2, t.numSquares(13))
log(1, t.numSquares(1))
log(3, t.numSquares(3))
log(2, t.numSquares(32456))
log(3, t.numSquares(43))
