# 121. Best Time to Buy and Sell Stock

# Say you have an array for which the ith element is the price of a
# given stock on day i.

# If you were only permitted to complete at most one transaction (i.e.,
# buy one and sell one share of the stock), design an algorithm to find
# the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# Example 2:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = float("inf"), None, 0
        for n in prices:
            if n < buy:
                buy = n
                sell = None
            elif n > buy:
                sell = max(n, sell) if sell is not None else n
                profit = max(profit, sell - buy)
        return profit

            # print(f"n = {n}, buy = {buy}, sell = {sell}, profit = {profit}")
def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(2, t.maxProfit([1,2,3,0,2]))
log(5, t.maxProfit([7,1,5,3,6,4]))
log(0, t.maxProfit([7,6,4,3,1]))
log(0, t.maxProfit([7,6,4,3,1]))
log(95, t.maxProfit([7,6,5,42,100,1,1,42,15]))
log(99, t.maxProfit([7,6,5,42,100,1,1,42,15,100]))