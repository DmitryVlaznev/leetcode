# 1007. Minimum Domino Rotations For Equal Row

# In a row of dominoes, A[i] and B[i] represent the top and bottom
# halves of the ith domino.  (A domino is a tile with two numbers from 1
# to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that A[i] and B[i] swap values.

# Return the minimum number of rotations so that all the values in A are
# the same, or all the values in B are the same.

# If it cannot be done, return -1.


# Example 1:
# Input:
# A = [2,1,2,4,2,2],
# B = [5,2,6,2,3,2]
# Output: 2
# Explanation:
# The first figure represents the dominoes as given by A and B: before
# we do any rotations. If we rotate the second and fourth dominoes, we
# can make every value in the top row equal to 2, as indicated by the
# second figure.

# Example 2:
# Input:
# A = [3,5,1,2,3],
# B = [3,6,3,3,4]
# Output: -1
# Explanation:
# In this case, it is not possible to rotate the dominoes to make one
# row of values equal.

# Constraints:
# 2 <= A.length == B.length <= 2 * 104
# 1 <= A[i], B[i] <= 6

from typing import List
from utils import checkValue


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a = A[0]
        b = B[0]

        a_a = 0  # fill the top row with A[0]
        b_b = 0  # fill the bottom row with B[0]
        a_b = 0 if a == b else 1  # fill the top row with B[0]
        b_a = 0 if a == b else 1  # fill the bottom row with A[0]
        for i in range(1, len(A)):
            if A[i] != a and A[i] != b and B[i] != a and B[i] != b:
                return -1
            if a_a is not None:
                if A[i] != a and B[i] != a:
                    a_a = None
                else:
                    a_a = a_a if A[i] == a else a_a + 1
            if a_b is not None:
                if A[i] != b and B[i] != b:
                    a_b = None
                else:
                    a_b = a_b if A[i] == b else a_b + 1
            if b_b is not None:
                if A[i] != b and B[i] != b:
                    b_b = None
                else:
                    b_b = b_b if B[i] == b else b_b + 1
            if b_a is not None:
                if A[i] != a and B[i] != a:
                    b_a = None
                else:
                    b_a = b_a if B[i] == a else b_a + 1

        if a_a is None and a_b is None and b_a is None and b_b is None:
            return -1
        res = float("inf")
        for r in [a_a, a_b, b_a, b_b]:
            if r is not None:
                res = min(res, r)
        return res


t = Solution()
checkValue(2, t.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]))
checkValue(-1, t.minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]))
checkValue(0, t.minDominoRotations([5, 5], [3, 6]))
checkValue(0, t.minDominoRotations([3], [2]))
