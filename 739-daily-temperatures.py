# 739. Daily Temperatures

# Medium

# Given an array of integers temperatures represents the daily
# temperatures, return an array answer such that answer[i] is the number
# of days you have to wait after the ith day to get a warmer
# temperature. If there is no future day for which this is possible,
# keep answer[i] == 0 instead.


# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]


# Constraints:
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, stack = [], []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if len(stack) == 0:
                res.append(0)
            else:
                res.append(stack[-1][0] - i)
            stack.append((i, temperatures[i]))
        return res[::-1]
