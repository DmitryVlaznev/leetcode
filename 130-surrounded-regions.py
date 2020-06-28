# 130. Surrounded Regions

# Given a 2D board containing 'X' and 'O' (the letter O), capture all
# regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.

# Example:

# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:

# Surrounded regions shouldn’t be on the border, which means that any
# 'O' on the border of the board are not flipped to 'X'. Any 'O' that is
# not on the border and it is not connected to an 'O' on the border will
# be flipped to 'X'. Two cells are connected if they are adjacent cells
# connected horizontally or vertically.

from typing import List


class Solution:
    def mark(self, board: List[List[str]], r, c, rows, cols):
        board[r][c] = "#"
        if r > 0 and board[r - 1][c] == "O":
            self.mark(board, r - 1, c, rows, cols)
        if r < rows - 1 and board[r + 1][c] == "O":
            self.mark(board, r + 1, c, rows, cols)
        if c > 0 and board[r][c - 1] == "O":
            self.mark(board, r, c - 1, rows, cols)
        if c < cols - 1 and board[r][c + 1] == "O":
            self.mark(board, r, c + 1, rows, cols)

    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        if rows == 0: return board
        cols = len(board[0])
        if cols == 0: return board

        for c in range(cols):
            if board[0][c] == "O": self.mark(board, 0, c, rows, cols)
            if board[rows - 1][c] == "O": self.mark(board, rows - 1, c, rows, cols)

        for r in range(1, rows):
            if board[r][0] == "O": self.mark(board, r, 0, rows, cols)
            if board[r][cols - 1] == "O": self.mark(board, r, cols - 1, rows, cols)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O": board[r][c] = "X"
                elif board[r][c] == "#": board[r][c] = "O"

t = Solution()
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
t.solve(board)
print(board)

board = [
    ["X", "O", "X", "X"],
]
t.solve(board)
print(board)

board = [
    ["X"],
    ["O"],
    ["X"],
    ["X"],
]
t.solve(board)
print(board)

board = [[]]
t.solve(board)
print(board)

board = []
t.solve(board)
print(board)