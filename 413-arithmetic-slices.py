# 413. Arithmetic Slices

# Medium

# A sequence of numbers is called arithmetic if it consists of at least
# three elements and if the difference between any two consecutive
# elements is the same.

# For example, these are arithmetic sequences:
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9

# The following sequence is not arithmetic.
# 1, 1, 2, 5, 7

# A zero-indexed array A consisting of N numbers is given. A slice of
# that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

# A slice (P, Q) of the array A is called arithmetic if the sequence:
# A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this
# meres that P + 1 < Q.

# The function should return the number of arithmetic slices in the
# array A.

# Example:
# A = [1, 2, 3, 4]
# return: 3,
# for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1,
# 2, 3, 4] itself.

from typing import List, Tuple
from utils import checkValue


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count, res, d = 0, 0, None
        for i in range(1, len(A)):
            cur_d = A[i] - A[i - 1]
            if cur_d == d:
                res += count
                count += 1
            else:
                d = cur_d
                count = 1
        return res


t = Solution()

checkValue(3, t.numberOfArithmeticSlices([1, 2, 3, 4]))
checkValue(0, t.numberOfArithmeticSlices([2, 1, 3, 4, 2, 3]))
checkValue(
    120, t.numberOfArithmeticSlices([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
)
checkValue(2, t.numberOfArithmeticSlices([1, 2, 3, 8, 9, 10]))
