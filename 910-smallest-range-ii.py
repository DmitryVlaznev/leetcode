# 910. Smallest Range II

# Medium

# Given an array A of integers, for each integer A[i] we need to choose
# either x = -K or x = K, and add x to A[i] (only once).

# After this process, we have some array B.

# Return the smallest possible difference between the maximum value of B
# and the minimum value of B.

# Example 1:
# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]

# Example 2:
# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]

# Example 3:
# Input: A = [1,3,6], K = 3
# Output: 3
# Explanation: B = [4,6,3]


# Note:
# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000

from typing import List
from utils import checkValue


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        if len(A) == 1:
            return 0
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            cur_max = max(A[i] + K, A[-1] - K)
            cur_min = min(A[0] + K, A[i + 1] - K)
            res = min(res, cur_max - cur_min)
        return res


t = Solution()

checkValue(0, t.smallestRangeII([1], 0))
checkValue(6, t.smallestRangeII([0, 10], 2))
checkValue(3, t.smallestRangeII([1, 3, 6], 3))
checkValue(3, t.smallestRangeII([1, 4, 6], 3))
