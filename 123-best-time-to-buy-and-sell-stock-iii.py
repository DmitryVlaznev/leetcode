# 123. Best Time to Buy and Sell Stock III

# Hard

# You are given an array prices where prices[i] is the price of a given
# stock on the ith day.

# Find the maximum profit you can achieve. You may complete at most two
# transactions.

# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# Example 4:
# Input: prices = [1]
# Output: 0


# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^5

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1, t2 = [0] * len(prices), [0] * len(prices)
        t1_min, t2_max = prices[0], prices[len(prices) - 1]
        l, r = 1, len(prices) - 2
        while l < len(prices) and r >= 0:
            profit1 = prices[l] - t1_min if prices[l] > t1_min else 0
            t1[l] = max(t1[l - 1], profit1)
            t1_min = min(t1_min, prices[l])

            profit2 = t2_max - prices[r] if t2_max > prices[r] else 0
            t2[r] = max(t2[r + 1], profit2)
            t2_max = max(t2_max, prices[r])

            l, r = l + 1, r - 1

        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, t1[i - 1] + t2[i], t2[i - 1], t1[i])
        return profit


s = Solution()
s.maxProfit([1, 2, 3, 4, 5])
