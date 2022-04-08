# 1155. Number of Dice Rolls With Target Sum

# Medium

# You have n dice and each die has k faces numbered from 1 to k.

# Given three integers n, k, and target, return the number of possible
# ways (out of the kn total ways) to roll the dice so the sum of the
# face-up numbers equals target. Since the answer may be too large,
# return it modulo 10^9 + 7.

# Example 1:
# Input: n = 1, k = 6, target = 3
# Output: 1
# Explanation: You throw one die with 6 faces.
# There is only one way to get a sum of 3.

# Example 2:
# Input: n = 2, k = 6, target = 7
# Output: 6
# Explanation: You throw two dice, each with 6 faces.
# There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

# Example 3:
# Input: n = 30, k = 30, target = 500
# Output: 222616187
# Explanation: The answer must be returned modulo 10^9 + 7.

# Constraints:
# 1 <= n, k <= 30
# 1 <= target <= 1000

from utils import checkValue


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for i in range(n + 1)]
        for i in range(1, min(k + 1, target + 1)):
            dp[1][i] = 1

        for rounds in range(2, n + 1):
            for t in range(1, target + 1):
                if t < rounds:
                    dp[rounds][t] == 0
                    continue
                for face in range(1, min(k + 1, t - rounds + 2)):
                    dp[rounds][t] = (dp[rounds][t] + dp[rounds - 1][t - face]) % (
                        10 ** 9 + 7
                    )
        return dp[-1][-1]


s = Solution()
checkValue(6, s.numRollsToTarget(2, 6, 7))
checkValue(1, s.numRollsToTarget(1, 6, 3))
checkValue(222616187, s.numRollsToTarget(30, 30, 500))
