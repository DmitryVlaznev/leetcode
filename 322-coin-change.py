# 322. Coin Change

# Medium

# You are given coins of different denominations and a total amount of
# money amount. Write a function to compute the fewest number of coins
# that you need to make up that amount. If that amount of money cannot
# be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

# Example 4:
# Input: coins = [1], amount = 1
# Output: 1

# Example 5:
# Input: coins = [1], amount = 2
# Output: 2

# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4

from typing import List
from utils import checkValue


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                dp[i] = min(dp[i], dp[i - c] + 1) if i - c >= 0 else dp[i]
        return dp[-1] if dp[-1] != float("inf") else -1

    def coinChangeCoins(self, coins: List[int], amount: int) -> List[int]:
        dp = [float("inf")] * (amount + 1)
        res = [[] for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0 and dp[i - c] != float("inf"):
                    if dp[i - c] + 1 < dp[i]:
                        dp[i] = dp[i - c] + 1
                        res[i] = res[i - c][:] + [c]
        return res[-1] if dp[-1] != float("inf") else []


s = Solution()
print(s.coinChangeCoins([1, 2, 5], 11))
print(s.coinChangeCoins([1], 1))
print(s.coinChangeCoins([2], 3))
