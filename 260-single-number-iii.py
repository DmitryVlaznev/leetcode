# 260. Single Number III

# Given an array of numbers nums, in which exactly two elements appear only once
# and all the other elements appear exactly twice. Find the two elements that
# appear only once.

# Example:

# Input:  [1,2,1,3,2,5]
# Output: [3,5]

# Note:
# * The order of the result is not important. So in the above example, [5, 3] is
#   also correct.
# * Your algorithm should run in linear runtime complexity. Could you implement
#   it using only constant space complexity?

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for n in nums: diff ^= n
        # now diff consist of different 1-nes of two target numbers
        # two's component (additional code) of this diff keeps the less
        # significant bit which is equals to 1
        tc = ~diff + 1
        bitmask = tc & diff
        # now the bitmask stores only the single 1 of one of the target numbers
        # lets just find it
        x = 0
        for n in nums:
            if n & bitmask: x ^= n
        return [x, x^diff]

t = Solution()
print(t.singleNumber([1,2,1,3,2,5]))
print(t.singleNumber([1,2,1,0,2,5]))
print(t.singleNumber([1,2]))