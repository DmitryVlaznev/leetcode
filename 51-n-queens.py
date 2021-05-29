# 51. N-Queens

# Hard

# The n-queens puzzle is the problem of placing n queens on an n x n
# chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens
# puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.


# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:
# Input: n = 1
# Output: [["Q"]]

# Constraints:
# 1 <= n <= 9

from typing import List


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

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        if n < 4:
            return []

        self.n = n
        self.findSolution([0] * n, [[0] * n for _ in range(n)], 0)
        res = []
        for queens in self.solutions:
            s = []
            for q in queens:
                row = ["."] * n
                row[q] = "Q"
                s.append("".join(row))
            res.append(s)
        return res
