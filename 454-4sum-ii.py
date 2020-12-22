# 454. 4Sum II

# Medium

# Given four lists A, B, C, D of integer values, compute how many tuples
# (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

# To make problem a bit easier, all A, B, C, D have same length of N
# where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1
# and the result is guaranteed to be at most 231 - 1.

# Example:
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# Output:
# 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

from typing import List


class Solution:
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        sums = {}
        for i in A:
            for j in B:
                if i + j not in sums:
                    sums[i + j] = 1
                else:
                    sums[i + j] += 1
        counter = 0
        for i in C:
            for j in D:
                if -1 * (i + j) in sums:
                    counter += sums[-1 * (i + j)]
        return counter