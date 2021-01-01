# 289. Game of Life

# Medium

# According to Wikipedia's article: "The Game of Life, also known simply
# as Life, is a cellular automaton devised by the British mathematician
# John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an
# initial state: live (represented by a 1) or dead (represented by a 0).
# Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above
# Wikipedia article):

# * Any live cell with fewer than two live neighbors dies as if caused
#   by under-population.
# * Any live cell with two or three live neighbors lives on to the next
#   generation.
# * Any live cell with more than three live neighbors dies, as if by
#   over-population.
# * Any dead cell with exactly three live neighbors becomes a live cell,
#   as if by reproduction.
# * The next state is created by applying the above rules simultaneously
#   to every cell in the current state, where births and deaths occur
#   simultaneously. Given the current state of the m x n grid board,
#   return the next state.


# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

# Example 2:
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]

# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.

# Follow up:
# Could you solve it in-place? Remember that the board needs to be
# updated simultaneously: You cannot update some cells first and then
# use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In
# principle, the board is infinite, which would cause problems when the
# active area encroaches upon the border of the array (i.e., live cells
# reach the border). How would you address these problems?

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                alive_neighbors = 0
                for p in range(i - 1, i + 2):
                    for q in range(j - 1, j + 2):
                        if p == i and q == j:
                            continue
                        if p < 0 or p >= rows or q < 0 or q >= cols:
                            continue
                        alive_neighbors += (
                            1 if board[p][q] == 1 or board[p][q] == 2 else 0
                        )
                if board[i][j] == 0 and alive_neighbors == 3:
                    board[i][j] = 3
                if board[i][j] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                    board[i][j] = 2
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1


t = Solution()

print("-------------")
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
t.gameOfLife(board)
print(board)
print([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])

print("-------------")
board = [[1, 1], [1, 0]]
t.gameOfLife(board)
print(board)
print([[1, 1], [1, 1]])
