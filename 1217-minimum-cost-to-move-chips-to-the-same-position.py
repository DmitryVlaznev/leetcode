# 1217. Minimum Cost to Move Chips to The Same Position

# We have n chips, where the position of the ith chip is position[i].

# We need to move all the chips to the same position. In one step, we
# can change the position of the ith chip from position[i] to:

# position[i] + 2 or position[i] - 2 with cost = 0.
# position[i] + 1 or position[i] - 1 with cost = 1.
# Return the minimum cost needed to move all the chips to the same position.

# Example 1:
# Input: position = [1,2,3]
# Output: 1
# Explanation: First step: Move the chip at position 3 to position 1
# with cost = 0.
# Second step: Move the chip at position 2 to position 1 with cost = 1.
# Total cost is 1.

# Example 2:
# Input: position = [2,2,2,3,3]
# Output: 2
# Explanation: We can move the two chips at poistion 3 to position 2.
# Each move has cost = 1. The total cost = 2.

# Example 3:
# Input: position = [1,1000000000]
# Output: 1

# Constraints:
# * 1 <= position.length <= 100
# * 1 <= position[i] <= 10^9

from typing import List
from utils import checkValue


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evens = odds = 0
        for c in position:
            if c % 2:
                odds += 1
            else:
                evens += 1
        return min(evens, odds)


t = Solution()

checkValue(1, t.minCostToMoveChips([1, 2, 3]))
checkValue(2, t.minCostToMoveChips([2, 2, 2, 3, 3]))
checkValue(1, t.minCostToMoveChips([1, 1000000000]))
checkValue(0, t.minCostToMoveChips([1, 13]))
checkValue(0, t.minCostToMoveChips([10, 130]))
checkValue(0, t.minCostToMoveChips([10]))
checkValue(0, t.minCostToMoveChips([]))