# 84. Largest Rectangle in Histogram

# Hard

# Given n non-negative integers representing the histogram's bar height
# where the width of each bar is 1, find the area of largest rectangle
# in the histogram.

#    0
#   HH
#   HH
#   HH 0
# 0 HH00
# 00HH00
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].

# The largest rectangle is shown in the shaded area, which has area = 10
# unit.

# Example:
# Input: [2,1,5,6,2,3]
# Output: 10

# 1) Create an empty stack.
# 2) Start from first bar, and do following for every bar ‘hist[i]’
#    where ‘i’ varies from 0 to n-1.
# ……a) If stack is empty or hist[i] is higher than the bar at top of
# stack, then push ‘i’ to stack.
# ……b) If this bar is smaller than the top of stack, then keep removing
# the top of stack while top of the stack is greater. Let the removed
# bar be hist[tp]. Calculate area of rectangle with hist[tp] as smallest
# bar. For hist[tp], the ‘left index’ is previous (previous to tp) item
# in stack and ‘right index’ is ‘i’ (current index).
# 3) If the stack is not empty, then one by one remove all bars from
#    stack and do step 2.b for every removed bar.

# Following is implementation of the above algorithm.

from typing import List
from utils import checkValue


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                top_idx = stack.pop()
                left = stack[-1] if stack else -1
                area = (i - left - 1) * heights[top_idx]
                max_area = max(max_area, area)
            stack.append(i)
        if stack:
            right = stack[-1] + 1
            while stack:
                top_idx = stack.pop()
                left = stack[-1] if stack else -1
                area = (right - left - 1) * heights[top_idx]
                max_area = max(max_area, area)
        return max_area


t = Solution()

checkValue(10, t.largestRectangleArea([2, 1, 5, 6, 2, 3]))
checkValue(4, t.largestRectangleArea([1, 2, 3]))
checkValue(10, t.largestRectangleArea([2, 4, 5, 3, 2]))
checkValue(4, t.largestRectangleArea([1, 4, 1]))
checkValue(3, t.largestRectangleArea([1, 2, 1]))
checkValue(4, t.largestRectangleArea([1, 2, 1, 1]))
checkValue(12, t.largestRectangleArea([2, 4, 5, 3, 4, 1]))
checkValue(9, t.largestRectangleArea([2, 4, 5, 3]))
checkValue(5, t.largestRectangleArea([5]))
checkValue(0, t.largestRectangleArea([]))
checkValue(4, t.largestRectangleArea([1, 4]))
checkValue(4, t.largestRectangleArea([4, 1]))
checkValue(4, t.largestRectangleArea([3, 2, 1]))
