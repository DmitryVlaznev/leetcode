# 1151. Minimum Swaps to Group All 1's Together

# Medium

# Given a binary array data, return the minimum number of swaps required
# to group all 1’s present in the array together in any place in the
# array.

# Example 1:
# Input: data = [1,0,1,0,1]
# Output: 1
# Explanation:
# There are 3 ways to group all 1's together:
# [1,1,1,0,0] using 1 swap.
# [0,1,1,1,0] using 2 swaps.
# [0,0,1,1,1] using 1 swap.
# The minimum is 1.

# Example 2:
# Input: data = [0,0,0,1,0]
# Output: 0
# Explanation:
# Since there is only one 1 in the array, no swaps needed.

# Example 3:
# Input: data = [1,0,1,0,1,0,0,1,1,0,1]
# Output: 3
# Explanation:
# One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].

# Example 4:
# Input: data = [1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]
# Output: 8

# Constraints:

# 1 <= data.length <= 105
# data[i] is 0 or 1.

from typing import List
from utils import checkValue


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        p, q, cur_ones = 0, ones - 1, sum(data[0:ones])
        max_ones = cur_ones
        while q < len(data) - 1:
            cur_ones -= data[p]
            cur_ones += data[q + 1]
            p, q = p + 1, q + 1
            if cur_ones > max_ones:
                max_ones = cur_ones
        return ones - max_ones


t = Solution()

checkValue(1, t.minSwaps([1, 0, 1, 0, 1]))
checkValue(0, t.minSwaps([0, 0, 0, 1, 0]))
checkValue(0, t.minSwaps([0, 1, 1, 1, 0]))
checkValue(0, t.minSwaps([1, 1, 1]))
checkValue(2, t.minSwaps([1, 1, 0, 0, 0, 0, 1, 1, 0, 1]))
checkValue(
    8,
    t.minSwaps(
        [
            1,
            0,
            1,
            0,
            1,
            0,
            1,
            1,
            1,
            0,
            1,
            0,
            0,
            1,
            1,
            1,
            0,
            0,
            1,
            1,
            1,
            0,
            1,
            0,
            1,
            1,
            0,
            0,
            0,
            1,
            1,
            1,
            1,
            0,
            0,
            1,
        ]
    ),
)
