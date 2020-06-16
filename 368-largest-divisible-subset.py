# 368. Largest Divisible Subset

# Given a set of distinct positive integers, find the largest subset
# such that every pair (Si, Sj) of elements in this subset satisfies:

# Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)

# Example 2:
# Input: [1,2,4,8]
# Output: [1,2,4,8]

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) < 1: return nums
        nums.sort()
        max_idx = 0
        divisors = [1 for i in range(len(nums))]
        prev = [-1 for i in range(len(nums))]

        for i, n in enumerate(nums):
            for j in range(i):
                if n % nums[j] == 0 and divisors[j] + 1 > divisors[i]:
                    divisors[i] = divisors[j] + 1
                    prev[i] = j
            if divisors[i] > divisors[max_idx]:
                max_idx = i

        res = []
        i = max_idx
        while i > -1:
            res.append(nums[i])
            i = prev[i]
        return res


def log(correct, res):
    if len(correct) == len(res) and set(correct) == set(res):
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()
log([1, 2], t.largestDivisibleSubset([1, 2, 3]))
log([1, 2, 4, 8], t.largestDivisibleSubset([1, 2, 4, 8]))
log([], t.largestDivisibleSubset([]))
log([1, 2, 4, 8], t.largestDivisibleSubset([3, 1, 8, 17, 4, 2]))
log([1, 3, 9, 27, 81], t.largestDivisibleSubset([1, 3, 2, 4, 8, 9, 27, 81]))
