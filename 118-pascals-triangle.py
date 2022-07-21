# 118. Pascal's Triangle

# Easy

# Given an integer numRows, return the first numRows of Pascal's
# triangle.

# In Pascal's triangle, each number is the sum of the two numbers
# directly above it as shown:


# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]


# Constraints:
# 1 <= numRows <= 30

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]] + [[] for _ in range(numRows - 1)]

        for r in range(1, numRows):
            for i in range(r + 1):
                left = res[r - 1][i - 1] if i > 0 else 0
                right = res[r - 1][i] if i < r else 0
                res[r].append(left + right)
        return res
