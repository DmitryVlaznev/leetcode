# 39. Combination Sum

# Given an array of distinct integers candidates and a target integer
# target, return a list of all unique combinations of candidates where
# the chosen numbers sum to target. You may return the combinations in
# any order.

# The same number may be chosen from candidates an unlimited number of
# times. Two combinations are unique if the frequency of at least one of
# the chosen numbers is different.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []

# Example 4:
# Input: candidates = [1], target = 1
# Output: [[1]]

# Example 5:
# Input: candidates = [1], target = 2
# Output: [[1,1]]

# Constraints:
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500

from typing import List, Set
import utils


class Solution:
    def findCombination(self, candidates: List[int], target: int, selected: List[int]):
        if target == 0:
            selected.sort()
            selected_hash = ",".join(str(s) for s in selected)
            if  selected_hash not in self.added:
                self.combinations.append(selected[:])
                self.added.add(selected_hash)
            return
        if target < 0: return

        for c in candidates:
            selected_with_c = selected[:]
            selected_with_c.append(c)
            self.findCombination(candidates, target - c, selected_with_c)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinations = []
        self.added = set()
        self.findCombination(candidates, target, [])
        return self.combinations

t = Solution()

utils.checkList([[2, 2, 3], [7]], t.combinationSum([2,3,6,7], 7))
utils.checkList([[2,2,2,2],[2,3,3],[3,5]], t.combinationSum([2,3,5], 8))
utils.checkList([], t.combinationSum([2], 1))
utils.checkList([[1]], t.combinationSum([1], 1))
utils.checkList([[1,1]], t.combinationSum([1], 2))
