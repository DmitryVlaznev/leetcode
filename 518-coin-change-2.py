# 518. Coin Change 2

# You are given coins of different denominations and a total amount of
# money. Write a function to compute the number of combinations that
# make up that amount. You may assume that you have infinite number of
# each kind of coin.


# Example 1:
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

# Example 3:
# Input: amount = 10, coins = [10]
# Output: 1

# Note:
# You can assume that
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not len(coins): return 1 if amount == 0 else 0
        cc = len(coins)
        dp = [[0 for x in range(cc)] for x in range(amount + 1)]
        for i in range(cc):
            dp[0][i] = 1

        for i in range(1, amount + 1):
            for j in range(cc):
                # Solutions including coins[j]
                x = dp[i - coins[j]][j] if i - coins[j] >= 0 else 0
                # Solutions excluding coins[j]
                y = dp[i][j - 1] if j >= 1 else 0
                # total count
                dp[i][j] = x + y
        return dp[amount][cc - 1]

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log(4, t.change(5, [1, 2, 5]))
log(0, t.change(3, [2]))
log(1, t.change(10, [10]))
log(12701, t.change(500, [1, 2, 5]))
log(0, t.change(0, []))
