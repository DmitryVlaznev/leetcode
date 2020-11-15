# 47. Permutations II

# Given a collection of numbers, nums, that might contain duplicates,
# return all possible unique permutations in any order.


# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Constraints:
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10

from typing import List


class Solution:
    unique = set()

    def peekOne(self, cur_sequence: str, rest: List[int]):
        if not rest:
            if cur_sequence not in self.unique:
                self.unique.add(cur_sequence)
            return
        for i, n in enumerate(rest):
            new_sequence = cur_sequence + "|" + str(n) if len(cur_sequence) else str(n)
            self.peekOne(new_sequence, rest[0:i] + rest[i + 1 :])

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.unique.clear()
        self.peekOne("", nums)
        return [[int(n) for n in s.split("|")] for s in self.unique]


t = Solution()
print(t.permuteUnique([1, 1, 2]))
print(t.permuteUnique([1, 1, 1]))
print(t.permuteUnique([1]))
