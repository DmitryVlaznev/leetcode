# N-Queens II

# Hard

# The n-queens puzzle is the problem of placing n queens on an n x n
# chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the
# n-queens puzzle.


# Example 1:
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle
# as shown.

# Example 2:
# Input: n = 1
# Output: 1

# Constraints:
# 1 <= n <= 9


class Solution:
    def __init__(self):
        self.solutions = set()
        self.n = 0

    def shade(self, board, row, col):
        shaded = [row[:] for row in board]
        left = right = col
        for r in range(row, self.n):
            shaded[r][col] = 1
            if left >= 0:
                shaded[r][left] = 1
            if right < self.n:
                shaded[r][right] = 1
            left, right = left - 1, right + 1
        return shaded

    def findSolution(self, queens, board, row):
        if row == self.n:
            self.solutions.add(tuple(queens))
            return
        for col in range(self.n):
            if board[row][col] != 1:
                q, b = queens[:], self.shade(board, row, col)
                q[row] = col
                self.findSolution(q, b, row + 1)

    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        if n < 4:
            return 0

        self.n = n
        self.findSolution([0] * n, [[0] * n for _ in range(n)], 0)
        return len(self.solutions)


t = Solution()
print(t.totalNQueens(5))