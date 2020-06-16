# 646. Maximum Length of Pair Chain

# You are given n pairs of numbers. In every pair, the first number is
# always smaller than the second number.

# Now, we define a pair (c, d) can follow another pair (a, b) if and
# only if b < c. Chain of pairs can be formed in this fashion.

# Given a set of pairs, find the length longest chain which can be
# formed. You needn't use up all the given pairs. You can select pairs
# in any order.

# Example 1:
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# Note:
# The number of given pairs will be in the range [1, 1000].

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if len(pairs) == 0: return 0
        pairs.sort(key=lambda x: x[0])
        dp = [1] * len(pairs)
        for i, p in enumerate(pairs):
            for j in range(i):
                if pairs[j][1] < p[0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(2, t.findLongestChain([[2,3], [3,4], [1,2]]))
log(1, t.findLongestChain([[2,3], [3,4], [1,5]]))
log(1, t.findLongestChain([[2,3]]))