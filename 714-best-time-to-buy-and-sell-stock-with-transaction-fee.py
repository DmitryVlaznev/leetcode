# 714. Best Time to Buy and Sell Stock with Transaction Fee

# Medium

# You are given an array prices where prices[i] is the price of a given
# stock on the ith day, and an integer fee representing a transaction
# fee.

# Find the maximum profit you can achieve. You may complete as many
# transactions as you like, but you need to pay the transaction fee for
# each transaction.

# Note: You may not engage in multiple transactions simultaneously
# (i.e., you must sell the stock before you buy again).


# Example 1:
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

# Example 2:
# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6

# Constraints:
# 1 < prices.length <= 5 * 104
# 0 < prices[i], fee < 5 * 104

from typing import List
from utils import checkValue


# At the end of the i-th day, we maintain cash, the maximum profit we
# could have if we did not have a share of stock, and hold, the maximum
# profit we could have if we owned a share of stock.

# To transition from the i-th day to the i+1-th day, we either sell our
# stock cash = max(cash, hold + prices[i] - fee) or buy a stock hold =
# max(hold, cash - prices[i]). At the end, we want to return cash. We
# can transform cash first without using temporary variables because
# selling and buying on the same day can't be better than just
# continuing to hold the stock.

# Пусть мы знаем, что в какой-то день можно иметь самое большее x_0
# прибыли и при этом не иметь акции или же x_1 прибыли и иметь акцию.
# Пусть в этот день акция стоит p.

# Тогда на следующий день эти значения будут:

# x_0' = max(x_0, x_1 + p - fee) -- можем либо ничего не делать, оставив
# предыдущий результат без акции, либо продать акцию
# x_1' = max(x_1, x_0 - p) -- можем либо ничего не делать, оставив
# предыдущий результат с акцией, либо купить акцию

# Инициализируем x_0 = 0 (прибыли в начале нет, акции тоже), x_1 = -inf
# (чтобы не обрабатывать особым образом начальную ситуацию до первой
# покупки).

# В конце берем максимум из двух чисел.

# Где именно вычитаем fee - на покупке или на продаже, неважно.


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash


t = Solution()
t.maxProfit([1, 4, 3, 6, 5, 8], 2)
