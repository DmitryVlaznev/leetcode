# 85. Maximal Rectangle

# Hard

# Given a rows x cols binary matrix filled with 0's and 1's, find the
# largest rectangle containing only 1's and return its area.


# Example 1:
# Input: matrix = [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.

# Example 2:
# Input: matrix = []
# Output: 0

# Example 3:
# Input: matrix = [["0"]]
# Output: 0

# Example 4:
# Input: matrix = [["1"]]
# Output: 1

# Example 5:
# Input: matrix = [["0","0"]]
# Output: 0

# Constraints:

# rows == matrix.length
# cols == matrix[i].length
# 0 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        res = 0
        dp = [[0] * len(matrix[0]) for _ in matrix]
        for ri, row in enumerate(matrix):
            for ci, v in enumerate(row):
                if v == "0":
                    continue

                w = dp[ri][ci] = dp[ri][ci - 1] + 1 if ci > 0 else 1

                for i in range(ri, -1, -1):
                    w = min(w, dp[i][ci])
                    res = max(res, w * (ri - i + 1))
        return res


s = Solution()

matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]

print(s.maximalRectangle(matrix))