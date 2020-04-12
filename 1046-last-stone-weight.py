#  Last Stone Weight

# We have a collection of stones, each stone has a positive integer
# weight.

# Each turn, we choose the two heaviest stones and smash them together.
# Suppose the stones have weights x and y with x <= y.  The result of
# this smash is:

# If x == y, both stones are totally destroyed;

# If x != y, the stone of weight x is totally destroyed, and the stone
# of weight y has new weight y-x.

# At the end, there is at most 1 stone left.  Return the weight of this
# stone (or 0 if there are no stones left.)

# Example 1:
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


# Note:
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heaviest = 0
        buckets = [0] * 1000
        for stone in stones:
            heaviest = max(heaviest, stone)
            buckets[stone] += 1

        p = heaviest
        x = y = None
        while True:
            while p >= 0 and buckets[p] == 0: p -= 1
            if p < 0: return 0
            y = p
            buckets[p] -= 1

            q = p
            while q >= 0 and buckets[q] == 0: q -= 1
            if q < 0: return y
            x = q
            buckets[q] -= 1

            new_stone = y - x
            if new_stone: buckets[new_stone] += 1

t = Solution()
print("1 = ", t.lastStoneWeight([2,7,4,1,8,1]))
print("7 = ", t.lastStoneWeight([7]))
print("0 = ", t.lastStoneWeight([]))
print("3 = ", t.lastStoneWeight([2, 5]))
print("498 = ", t.lastStoneWeight([2, 500]))
