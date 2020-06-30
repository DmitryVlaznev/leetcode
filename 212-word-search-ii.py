# 212. Word Search II

# Given a 2D board and a list of words from the dictionary, find all
# words in the board.

# Each word must be constructed from letters of sequentially adjacent
# cell, where "adjacent" cells are those horizontally or vertically
# neighboring. The same letter cell may not be used more than once in a
# word.


# Example:
# Input:
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]

# Output: ["eat","oath"]

# Note:
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.

from typing import List


class Trie:
    def __init__(self):
        self.root = {"leaf": False, "children": {}}

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter in node["children"]:
                node = node["children"][letter]
            else:
                node["children"][letter] = {"leaf": False, "children": {}}
                node = node["children"][letter]
        node["leaf"] = True

    def search(self, word: str) -> bool:
        node = self.findNode(word)
        return node["leaf"] if node is not None else False

    def startsWith(self, prefix: str) -> bool:
        return self.findNode(prefix) is not None

    def findNode(self, prefix: str):
        node = self.root
        for letter in prefix:
            if letter not in node["children"]:
                return None
            else:
                node = node["children"][letter]
        return node


class Solution:
    def backtrack(self, row, col, board, prefix, trie, res):
        prefix += board[row][col]
        letter, board[row][col] = board[row][col], "#"
        if not trie.startsWith(prefix):
            return
        if trie.search(prefix):
            res.add(prefix)

        if row > 0 and board[row - 1][col] != "#":
            self.backtrack(row - 1, col, [r[:] for r in board], prefix, trie, res)
        if row < len(board) - 1 and board[row + 1][col] != "#":
            self.backtrack(row + 1, col, [r[:] for r in board], prefix, trie, res)
        if col > 0 and board[row][col - 1] != "#":
            self.backtrack(row, col - 1, [r[:] for r in board], prefix, trie, res)
        if col < len(board[0]) - 1 and board[row][col + 1] != "#":
            self.backtrack(row, col + 1, [r[:] for r in board], prefix, trie, res)

        board[row][col] = letter

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)

        res = set()
        board_copy = [r[:] for r in board]
        for row in range(len(board)):
            for col in range(len(board[0])):
                board_copy = [r[:] for r in board]
                self.backtrack(row, col, board_copy, "", trie, res)
        return list(res)


def log(correct, res):
    if len(correct) == len(res) and set(correct) == set(res):
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

board = [["a","b"],["c","d"]]
words = ["cdba"]
log(["cdba"], t.findWords(board, words))

board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]
log(["eat", "oath"], t.findWords(board, words))

board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "oathf", "eat", "rain"]
log(["eat", "oath", "oathf"], t.findWords(board, words))

board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = []
log([], t.findWords(board, words))

board = [
    ["o"],
]
words = ["tratata"]
log([], t.findWords(board, words))

board = [
    [],
]
words = ["tratata"]
log([], t.findWords(board, words))

board = []
words = ["tratata"]
log([], t.findWords(board, words))

board = []
words = []
log([], t.findWords(board, words))

board = [["a","a"]]
words = ["a"]
log(["a"], t.findWords(board, words))