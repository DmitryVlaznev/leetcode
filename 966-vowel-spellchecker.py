# 966. Vowel Spellchecker

# Medium

# Given a wordlist, we want to implement a spellchecker that converts a
# query word into a correct word.

# For a given query word, the spell checker handles two categories of
# spelling mistakes:

# Capitalization: If the query matches a word in the wordlist
# (case-insensitive), then the query word is returned with the same case
# as the case in the wordlist.
# Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
# Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
# Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"

# Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u')
# of the query word with any vowel individually, it matches a word in
# the wordlist (case-insensitive), then the query word is returned with
# the same case as the match in the wordlist.
# Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
# Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
# Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)

# In addition, the spell checker operates under the following precedence
# rules:
# * When the query exactly matches a word in the wordlist
#   (case-sensitive), you should return the same word back.
# * When the query matches a word up to capitalization, you should
#   return the first such match in the wordlist.
# * When the query matches a word up to vowel errors, you should return
#   the first such match in the wordlist.
# * If the query has no matches in the wordlist, you should return the
#   empty string.
# * Given some queries, return a list of words answer, where answer[i]
#   is the correct word for query = queries[i].

# Example 1:
# Input: wordlist = ["KiTe","kite","hare","Hare"], queries =
# ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

# Note:
# 1 <= wordlist.length <= 5000
# 1 <= queries.length <= 5000
# 1 <= wordlist[i].length <= 7
# 1 <= queries[i].length <= 7
# All strings in wordlist and queries consist only of english letters.

from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set(["a", "e", "i", "o", "u"])
        trie_lc = {"children": {}, "words": []}
        trie_wov = {"children": {}, "words": []}

        for word in wordlist:
            p = trie_lc
            q = trie_wov
            for letter in word:
                letter = letter.lower()
                if letter not in p["children"]:
                    p["children"][letter] = {"children": {}, "words": []}
                p = p["children"][letter]

                if letter in vowels:
                    letter = "*"
                if letter not in q["children"]:
                    q["children"][letter] = {"children": {}, "words": []}
                q = q["children"][letter]
            p["words"].append(word)
            q["words"].append(word)

        res = []
        wordlist = set(wordlist)
        for word in queries:
            if word in wordlist:
                res.append(word)
                continue

            p = trie_lc
            for i, letter in enumerate(word):
                letter = letter.lower()
                if letter not in p["children"]:
                    break
                p = p["children"][letter]

            if i == len(word) - 1 and p["words"]:
                res.append(p["words"][0])
                continue

            p = trie_wov
            for i, letter in enumerate(word):
                letter = letter.lower()
                if letter in vowels:
                    letter = "*"
                if letter not in p["children"]:
                    break
                p = p["children"][letter]

            if i == len(word) - 1 and p["words"]:
                res.append(p["words"][0])
            else:
                res.append("")
        return res

    def spellchecker_hashes(self, wordlist, queries):
        def devowel(word):
            return "".join("*" if c in "aeiou" else c for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return map(solve, queries)


t = Solution()
print(["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"])
print(
    t.spellchecker(
        ["KiTe", "kite", "hare", "Hare"],
        [
            "kite",
            "Kite",
            "KiTe",
            "Hare",
            "HARE",
            "Hear",
            "hear",
            "keti",
            "keet",
            "keto",
        ],
    )
)
