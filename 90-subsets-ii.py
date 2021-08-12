# 90. Subsets II

# Medium

# Given an integer array nums that may contain duplicates, return all
# possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the
# solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10

from typing import List
from functools import lru_cache


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        @lru_cache(maxsize=None)
        def getSubsetsFrom(idx):
            if idx >= len(nums):
                return tuple()
            nxt = getSubsetsFrom(idx + 1)
            r = []
            r.append(tuple([nums[idx]]))
            for seq in nxt:
                r.append(tuple(seq))
                r.append(tuple([nums[idx]] + list(seq)))
            return r

        return [[]] + list(map(list, set(getSubsetsFrom(0))))


s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
