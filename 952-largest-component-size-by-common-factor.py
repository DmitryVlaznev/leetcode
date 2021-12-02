# 952. Largest Component Size by Common Factor

# Hard

# You are given an integer array of unique positive integers nums.
# Consider the following graph:

# * There are nums.length nodes, labeled nums[0] to nums[nums.length -
#   1],
# * There is an undirected edge between nums[i] and nums[j] if nums[i]
#   and nums[j] share a common factor greater than 1.
# * Return the size of the largest connected component in the graph.


# Example 1:
# Input: nums = [4,6,15,35]
# Output: 4

# Example 2:
# Input: nums = [20,50,9,63]
# Output: 2

# Example 3:
# Input: nums = [2,3,6,7,4,12,21,39]
# Output: 8


# Constraints:
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] <= 10^5
# All the values of nums are unique.

from utils import checkValue
from typing import List
from collections import defaultdict, Counter


class UnionFind:
    def __init__(self, size):
        self.parents = list(range(size))

    def union(self, a, b):
        self.parents[self.root(a)] = self.parents[self.root(b)]

    def root(self, a):
        while self.parents[a] != a:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def prime_divisors(num):
            factor = 2
            prime_factors = set()
            while num >= factor * factor:
                if num % factor == 0:
                    prime_factors.add(factor)
                    num = num // factor
                else:
                    factor += 1
            prime_factors.add(num)
            return list(prime_factors)

        uf = UnionFind(len(nums))
        factors = defaultdict(list)
        for i, n in enumerate(nums):
            ff = prime_divisors(n)
            for f in ff:
                factors[f].append(i)

        for _, indices in factors.items():
            for i in range(1, len(indices)):
                uf.union(indices[i - 1], indices[i])

        return max(Counter([uf.root(i) for i in range(len(nums))]).values())


s = Solution()

checkValue(4, s.largestComponentSize([4, 6, 15, 35]))
checkValue(2, s.largestComponentSize([20, 50, 9, 63]))
checkValue(8, s.largestComponentSize([2, 3, 6, 7, 4, 12, 21, 39]))
