# 309. Best Time to Buy and Sell Stock with Cooldown

# Say you have an array for which the ith element is the price of a
# given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as
# many transactions as you like (ie, buy one and sell one share of the
# stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you
# must sell the stock before you buy again).

# After you sell your stock, you cannot buy stock on next day. (ie,
# cooldown 1 day)

# Example:
# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, waited = float('-inf'), float('-inf'), 0

        for price in prices:
            current_sold = sold
            sold = held + price
            held = max(held, waited - price)
            waited = max(waited, current_sold)
        return max(waited, sold)

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(3, t.maxProfit([1,2,3,0,2]))