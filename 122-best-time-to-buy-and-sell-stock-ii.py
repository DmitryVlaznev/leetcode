# 122. Best Time to Buy and Sell Stock II

# Say you have an array for which the ith element is the price of a
# given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as
# many transactions as you like (i.e., buy one and sell one share of the
# stock multiple times).

# Note: You may not engage in multiple transactions at the same time
# (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5),
#              profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell
#              on day 5 (price = 6), profit = 6-3 = 3.

# Example 2:
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5),
#              profit = 5-1 = 4. Note that you cannot buy on day 1, buy
#              on day 2 and sell them later, as you are engaging
#              multiple transactions at the same time. You must sell
#              before buying again.

# Example 3:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit =
# 0.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = None

        day = 0
        period = len(prices)
        while day < period - 1:
            if buy_price == None:
                buy_price = prices[day] if prices[day + 1] > prices[day] else None
            else:
                if prices[day + 1] < prices[day]:
                    profit += (prices[day] - buy_price)
                    buy_price = None
            day += 1

        profit = profit + (prices[period - 1] - buy_price) if buy_price != None else profit
        return profit

t = Solution()

print("7 = ", t.maxProfit([7,1,5,3,6,4]))
print("4 = ", t.maxProfit([1,2,3,4,5]))
print("0 = ", t.maxProfit([7,6,4,3,1]))
print("6 = ", t.maxProfit([0,6,4,3,1]))

def checkOverlap(self, r, xc, yc, x1, y1, x2, y2):
    a = (xc-max(x1,min(xc,x2)))**2
    b = (yc-max(y1,min(yc,y2)))**2
    return r*r >= a + b