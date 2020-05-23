# 1277. Count Square Submatrices with All Ones

# Given a m * n matrix of ones and zeros, return how many square
# submatrices have all ones.


# Example 1:
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation:
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.

# Example 2:
# Input: matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation:
# There are 6 squares of side 1.
# There is 1 square of side 2.
# Total number of squares = 6 + 1 = 7.


# Constraints:
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        squares = 0
        dp = [[0] * (cols + 1) for i in range(rows + 1)]
        for i in range(rows):
            r = i + 1
            for j in range(cols):
                c = j + 1
                if matrix[i][j] == 1:
                    dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1
                    squares += dp[r][c]

        return squares

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

m = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
log(15, t.countSquares(m))

m = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
log(7, t.countSquares(m))

m = [
  [1,0,1],
  [0,1,0],
  [1,0,0]
]
log(4, t.countSquares(m))

m = [
  [0,0,0],
  [0,0,0],
  [0,0,0]
]
log(0, t.countSquares(m))

m = [
  [0,0,1],
]
log(1, t.countSquares(m))

m = [
  [0],
  [1],
  [1]
]
log(2, t.countSquares(m))

m = [[0]]
log(0, t.countSquares(m))

m = [[1]]
log(1, t.countSquares(m))



