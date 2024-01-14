# 1424. Diagonal Traverse II

# Medium

# Given a 2D integer array nums, return all elements of nums in diagonal
# order as shown in the below images.


# Example 1:
# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]

# Example 2:
# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]


# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i].length <= 10^5
# 1 <= sum(nums[i].length) <= 10^5
# 1 <= nums[i][j] <= 10^5

from typing import List
import functools
from collections import deque


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dq, res = deque([(0, 0)]), []
        while dq:
            l = len(dq)
            while l:
                row, col = dq.popleft()
                res.append(nums[row][col])

                if col == 0 and row + 1 < len(nums):
                    dq.append((row + 1, col))

                if col + 1 < len(nums[row]):
                    dq.append((row, col + 1))
                l -= 1

        return res

    def findDiagonalOrder2(self, nums: List[List[int]]) -> List[int]:
        flatten = []
        for row in range(len(nums)):
            for col, val in enumerate(nums[row]):
                flatten.append((row + col, row, val))

        def cmp(a, b):
            if a[0] == b[0]:
                return -1 if a[1] > b[1] else 1
            return -1 if a[0] < b[0] else 1

        flatten.sort(key=functools.cmp_to_key(cmp))
        return list(map(lambda n: n[2], flatten))


s = Solution()
s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
