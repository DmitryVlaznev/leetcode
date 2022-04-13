# 1258. Synonymous Sentences

# Medium

# You are given a list of equivalent string pairs synonyms where
# synonyms[i] = [si, ti] indicates that si and ti are equivalent
# strings. You are also given a sentence text.

# Return all possible synonymous sentences sorted lexicographically.

# Example 1:
# Input: synonyms =
# [["happy","joy"],["sad","sorrow"],["joy","cheerful"]], text = "I am
# happy today but was sad yesterday"
# Output: ["I am cheerful today but was sad yesterday","I am cheerful
# today but was sorrow yesterday","I am happy today but was sad
# yesterday","I am happy today but was sorrow yesterday","I am joy today
# but was sad yesterday","I am joy today but was sorrow yesterday"]

# Example 2:
# Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am
# happy today but was sad yesterday"
# Output: ["I am happy today but was sad yesterday","I am joy today but
# was sad yesterday"]

# Constraints:
# 0 <= synonyms.length <= 10
# synonyms[i].length == 2
# 1 <= si.length, ti.length <= 10
# si != ti
# text consists of at most 10 words.
# The words of text are separated by single spaces.

from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, words):
        self.size = len(words)
        self.words = words
        self.wi = {words[i]: i for i in range(len(words))}
        self.parents = [i for i in range(len(words))]

    def find(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        return i

    def union(self, a, b):
        self.parents[self.find(self.wi[a])] = self.parents[self.find(self.wi[b])]

    def get_synonyms(self):
        s = defaultdict(list)
        for i in range(self.size):
            s[self.find(self.parents[i])].append(self.words[i])
        res = defaultdict(list)
        for group in s:
            s[group].sort()
            for w in s[group]:
                res[w] = s[group]
        return res


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        words = set()
        for a, b in synonyms:
            words.add(a)
            words.add(b)
        uf = UnionFind(list(words))
        for a, b in synonyms:
            uf.union(a, b)

        graph = uf.get_synonyms()

        text = text.split(" ")
        res = []

        def backtrack(i: int, phrase: List[str]):
            if i == len(text):
                res.append(" ".join(phrase))
                return

            word = text[i]
            if word in graph:
                s = graph[word]
                for w in s:
                    phrase.append(w)
                    backtrack(i + 1, phrase[:])
                    phrase.pop()
            else:
                phrase.append(word)
                backtrack(i + 1, phrase)

        backtrack(0, [])
        return res


s = Solution()
print(
    s.generateSentences(
        [["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]],
        "I am happy today but was sad yesterday",
    )
)
