# 79. Word Search

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent
# cell, where "adjacent" cells are those horizontally or vertically
# neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

from typing import List
class Solution:
    def dfs(self, board: List[List[str]], row: int, col: int, word: str, visited: set) -> bool:
        if len(word) == 0:
            return True

        firstLetter = word[0]

        up = str(row - 1) + "|" + str(col)
        if row > 0 and board[row - 1][col] == firstLetter and not up in visited:
            visited.add(up)
            if self.dfs(board, row - 1, col, word[1:], visited):
                return True
            visited.remove(up)

        down =  str(row + 1) + "|" + str(col)
        if row < len(board) - 1 and board[row + 1][col] == firstLetter and not down in visited:
            visited.add(down)
            if self.dfs(board, row + 1, col, word[1:], visited):
                return True
            visited.remove(down)

        left =  str(row) + "|" + str(col - 1)
        if col > 0 and board[row][col - 1] == firstLetter and not left in visited:
            visited.add(left)
            if self.dfs(board, row, col - 1, word[1:], visited):
                return True
            visited.remove(left)

        right =  str(row) + "|" + str(col + 1)
        if col < len(board[row]) - 1 and board[row][col + 1] == firstLetter and not right in visited:
            visited.add(right)
            if self.dfs(board, row, col + 1, word[1:], visited):
                return True
            visited.remove(right)

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not len(word):
            return True

        firstLetter = word[0]
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] != firstLetter:
                    continue
                visited = set()
                visited.add(str(row) + "|" + str(col))
                if self.dfs(board, row, col, word[1:], visited):
                    return True
        return False

test = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print("True = ", test.exist(board, "ABCCED"))
print("True = ", test.exist(board, "SEE"))
print("True = ", test.exist(board, ""))
print("False = ", test.exist(board, "ABCB"))
print("False = ", test.exist(board, "AE"))

board2 = [['A','B','C','E']]
print("True = ", test.exist(board2, "BC"))
print("False = ", test.exist(board2, "BD"))

board3 = [
  ['A'],
  ['S'],
  ['A']
]
print("True = ", test.exist(board3, "SA"))
print("False = ", test.exist(board3, "BD"))

board4 = [['A']]
print("True = ", test.exist(board4, "A"))
print("False = ", test.exist(board4, "BD"))

board5 = [[]]
print("True = ", test.exist(board5, ""))
print("False = ", test.exist(board5, "BD"))

board6 = [["a", "a"]]
print("False = ", test.exist(board6, "aaa"))