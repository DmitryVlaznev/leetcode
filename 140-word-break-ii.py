# 140. Word Break II

# Given a non-empty string s and a dictionary wordDict containing a list
# of non-empty words, add spaces in s to construct a sentence where each
# word is a valid dictionary word. Return all such possible sentences.

# Note:

# The same word in the dictionary may be reused multiple times in the
# segmentation. You may assume the dictionary does not contain duplicate
# words.

# Example 1:
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]

# Example 2:
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []

from typing import List


class Trie:
    def __init__(self):
        self.root = {"leaf": False, "children": {}}

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter in node["children"]: node =  node["children"][letter]
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
            if letter not in node["children"]: return None
            else: node = node["children"][letter]
        return node

class Solution:
    def parseString(self, input: str, trie: Trie, memo):
        if input in memo: return memo[input]
        letter = 1
        res = []
        while letter <= len(input) and trie.startsWith(input[:letter]):
            word = input[:letter]
            rest = input[letter:]
            if trie.search(word):
                if not rest:
                    tmp_res = [word]
                else:
                    if rest in memo:
                        tmp_res = memo[rest][:]
                    else:
                        tmp_res = self.parseString(rest, trie, memo)

                    for i, s in enumerate(tmp_res):
                        tmp_res[i] = " ".join([word, tmp_res[i]])
                res = res + tmp_res
            letter += 1
        memo[input] = res[:]
        return res

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict: return []
        trie = Trie()
        for word in wordDict: trie.insert(word)
        return self.parseString(s, trie, {})

t = Solution()
print(t.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(t.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
print(t.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(t.wordBreak("catsandog", []))
print(t.wordBreak("", ["cats", "dog", "sand", "and", "cat"]))

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(t.wordBreak(s, words))