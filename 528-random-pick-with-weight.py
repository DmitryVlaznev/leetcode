# 528. Random Pick with Weight

# Given an array w of positive integers, where w[i] describes the weight
# of index i, write a function pickIndex which randomly picks an index
# in proportion to its weight.

# Note:
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.

# Example 1:
# Input:
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]

# Example 2:
# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# Explanation of Input Syntax:

# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has one argument, the array w. pickIndex has no
# arguments. Arguments are always wrapped with a list, even if there
# aren't any.

from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.prefix = w[:]
        for i in range(1, len(w)):
            self.prefix[i] += self.prefix[i - 1]

    def pickIndex(self) -> int:
        length = len(self.prefix)
        if length == 1:
            return 0
        l = -1
        r = length
        import random

        target = random.random() * self.prefix[-1]
        while r - l > 1:
            mid = l + (r - l) // 2
            if self.prefix[mid] < target:
                l = mid
            else:
                r = mid
        return r if r < length else l


print("----------")
print([20, 50, 5, 25])
t = Solution([20, 50, 5, 25])
res = [0] * 4
for i in range(10000):
    res[t.pickIndex()] += 1
print([i / 100 for i in res])
print(res)