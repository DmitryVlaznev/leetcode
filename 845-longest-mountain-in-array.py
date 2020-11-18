# 845. Longest Mountain in Array

# Medium

# Let's call any (contiguous) subarray B (of A) a mountain if the
# following properties hold:

# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ...
# B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)

# Given an array A of integers, return the length of the longest
# mountain.
# Return 0 if there is no mountain.

# Example 1:
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:

# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
# Note:

# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000

# Follow up:
# Can you solve it using only one pass?
# Can you solve it in O(1) space?

from typing import List
from utils import checkValue


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        longest = 0
        start = 0
        top = -1

        for i, n in enumerate(A[1:]):
            if n > A[i]:
                if top > -1:
                    longest = max(longest, i + 1 - start)
                    start = i
                    top = -1
            elif n < A[i]:
                if top == -1:
                    if i > start:
                        top = i
                    else:
                        start = i + 1
                        top = -1
            else:
                if top > -1:
                    longest = max(longest, i + 1 - start)
                start = i + 1
                top = -1
        if top > 0 and top < len(A) - 1:
            longest = max(longest, len(A) - start)

        return longest if longest >= 3 else 0


t = Solution()
checkValue(5, t.longestMountain([2, 1, 4, 7, 3, 2, 5]))
checkValue(0, t.longestMountain([1, 4, 7, 12]))
checkValue(0, t.longestMountain([13, 8, 7, 1]))
checkValue(0, t.longestMountain([2, 1, 4]))
checkValue(3, t.longestMountain([2, 10, 4]))
checkValue(0, t.longestMountain([2, 10]))
checkValue(0, t.longestMountain([2, 2, 2]))
checkValue(5, t.longestMountain([2, 2, 2, 7, 8, 6, 2, 2, 2]))
checkValue(5, t.longestMountain([2, 7, 8, 6, 2, 2, 2]))
checkValue(5, t.longestMountain([2, 1, 4, 7, 3, 2]))
checkValue(5, t.longestMountain([2, 2, 2, 7, 8, 6, 2]))
checkValue(4, t.longestMountain([875, 884, 239, 731, 723, 685]))
