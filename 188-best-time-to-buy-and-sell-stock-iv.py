# 188. Best Time to Buy and Sell Stock IV

# You are given an integer array prices where prices[i] is the price of
# a given stock on the ith day.

# Design an algorithm to find the maximum profit. You may complete at
# most k transactions.

# Notice that you may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

# Example 2:
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6),
# profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6
# (price = 3), profit = 3-0 = 3.

# Constraints:
# 0 <= k <= 109
# 0 <= prices.length <= 104
# 0 <= prices[i] <= 1000

from typing import List
from utils import checkValue

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2 or k == 0: return 0
        buy_price, buy_day, deals = None, None, []

        day = 0
        while day < len(prices) - 1:
            if buy_price == None:
                buy_price = prices[day] if prices[day + 1] > prices[day] else None
                buy_day = day
            else:
                if prices[day + 1] < prices[day]:
                    deals.append([prices[buy_day], prices[day]])
                    buy_price, buy_day = None, None
            day += 1

        if buy_price != None: deals.append([prices[buy_day], prices[-1]])

        while len(deals) > k:
            merge_impact, merge_first = float("inf"), 0
            del_impact, del_first = float("inf"), 0
            for i in range(len(deals) - 1):
                merge_diff = (deals[i][1] - deals[i][0]) + (deals[i + 1][1] - deals[i + 1][0]) - (deals[i + 1][1] - deals[i][0])
                if merge_diff < merge_impact: merge_impact, merge_first = merge_diff, i
                del_diff = deals[i][1] - deals[i][0]
                if (del_diff < del_impact): del_impact, del_first = del_diff, i

            del_diff = deals[-1][1] - deals[-1][0]
            if (del_diff < del_impact): del_impact, del_first = del_diff, len(deals) - 1


            if merge_impact < del_impact:
                deals[merge_first][1] = deals[merge_first + 1][1]
                deals.pop(merge_first + 1)
            else:
                deals.pop(del_first)

        profit = 0
        for d in deals: profit += d[1] - d[0]
        return profit

t = Solution()
checkValue(2, t.maxProfit(2, [2,4,1]))
checkValue(7, t.maxProfit(2, [3,2,6,5,0,3]))
checkValue(4, t.maxProfit(1, [3,2,6,5,0,3]))
checkValue(0, t.maxProfit(0, [3,2,6,5,0,3]))
checkValue(0, t.maxProfit(10, [3]))
checkValue(0, t.maxProfit(10, []))
checkValue(13, t.maxProfit(2, [1,2,4,2,5,7,2,4,9,0]))