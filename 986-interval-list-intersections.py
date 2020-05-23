# 986. Interval List Intersections
# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# (Formally, a closed interval [a, b] (with a <= b) denotes the set of
# real numbers x with a <= x <= b.  The intersection of two closed
# intervals is a set of real numbers that is either empty, or can be
# represented as a closed interval.  For example, the intersection of
# [1, 3] and [2, 4] is [2, 3].)

# Example 1:
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

# Note:
# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        p, q = 0, 0
        x, y = None, None
        res = []
        while p < len(A) and q < len(B):
            if A[p][0] <= B[q][0]:
                x = A[p]
                y = B[q]
            else:
                x = B[q]
                y = A[p]
            if x[1] >= y[0]:
                res.append([max(x[0], y[0]), min(x[1], y[1])])
            if A[p][1] <= B[q][1]: p+= 1
            else: q+= 1
        return res

t = Solution()

print("---")
print([[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])
print(t.intervalIntersection(
    [[0,2],[5,10],[13,23],[24,25]],
    [[1,5],[8,12],[15,24],[25,26]])
)
print("")

print("---")
print([])
print(t.intervalIntersection(
    [],
    [[1,5],[8,12],[15,24],[25,26]])
)
print("")

print("---")
print([[1, 5], [8, 12], [15, 24], [25, 25], [26, 26]])
print(t.intervalIntersection(
    [[1, 25], [26,26]],
    [[1,5],[8,12],[15,24],[25,26]])
)
print("")