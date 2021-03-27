# 870. Advantage Shuffle

# Medium

# Given two arrays A and B of equal size, the advantage of A with
# respect to B is the number of indices i for which A[i] > B[i].

# Return any permutation of A that maximizes its advantage with respect
# to B.

# Example 1:
# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]

# Example 2:
# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]

# Note:
# 1 <= A.length = B.length <= 10000
# 0 <= A[i] <= 10^9
# 0 <= B[i] <= 10^9

from typing import List
from utils import checkList


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        a_sorted, b_sorted = A[:], B[:]
        a_sorted.sort()
        b_sorted.sort()

        covers = {}
        stack = []
        a = b = 0
        while b < len(B):
            if b_sorted[b] not in covers:
                covers[b_sorted[b]] = []
            if a < len(A):
                if a_sorted[a] > b_sorted[b]:
                    covers[b_sorted[b]].append(a_sorted[a])
                    a, b = a + 1, b + 1
                else:
                    stack.append(a_sorted[a])
                    a += 1
            else:
                covers[b_sorted[b]].append(stack.pop())
                b += 1
        res = []
        for n in B:
            res.append(covers[n].pop())
        return res


t = Solution()

print([1, 10, 4, 11])
print(t.advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))

print([13, 25, 32, 11])
print(t.advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))
