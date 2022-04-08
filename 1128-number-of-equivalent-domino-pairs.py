# 1128. Number of Equivalent Domino Pairs

# Easy

# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to
# dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a
# == d and b == c) - that is, one domino can be rotated to be equal to
# another domino.

# Return the number of pairs (i, j) for which 0 <= i < j <
# dominoes.length, and dominoes[i] is equivalent to dominoes[j].


# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1

# Example 2:
# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3

# Constraints:
# 1 <= dominoes.length <= 4 * 10^4
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9

from typing import List
from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen, res = defaultdict(lambda: 0), 0
        for d in dominoes:
            a, b = d
            if a > b:
                a, b = b, a
            res += seen[(a, b)]
            seen[(a, b)] += 1
        return res