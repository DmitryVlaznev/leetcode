# 211. Design Add and Search Words Data Structure

# Medium


# Design a data structure that supports adding new words and finding if
# a string matches any previously added string.

# Implement the WordDictionary class:
# * WordDictionary() Initializes the object.
# * void addWord(word) Adds word to the data structure, it can be
#   matched later.
# * bool search(word) Returns true if there is any string in the data
#   structure that matches word or false otherwise. word may contain
#   dots '.' where dots can be matched with any letter.


# Example:
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True


# Constraints:
# 1 <= word.length <= 500
# word in addWord consists lower-case English letters.
# word in search consist of  '.' or lower-case English letters.
# At most 50000 calls will be made to addWord and search.


class TrieDots:
    def __init__(self):
        self.data = {"leaf": False, "children": {}}

    def add(self, word: str):
        p = self.data
        for l in word:
            if l not in p["children"]:
                p["children"][l] = {"leaf": False, "children": {}}
            p = p["children"][l]
        p["leaf"] = True

    def check(self, word: str):
        return self._check(word, self.data)

    def _check(self, word: str, root):
        if not len(word):
            return root["leaf"]

        p = root
        for i in range(len(word)):
            l = word[i]
            if l == ".":
                rest = word[i + 1 :]
                return any([self._check(rest, node) for node in p["children"].values()])

            if l not in p["children"]:
                return False
            p = p["children"][l]
        return p["leaf"]


class WordDictionary:
    def __init__(self):
        self.t = TrieDots()

    def addWord(self, word: str) -> None:
        self.t.add(word)

    def search(self, word: str) -> bool:
        return self.t.check(word)


wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
print(wd.search("pad"))
print(wd.search("bad"))
print(wd.search(".ad"))
print(wd.search("b.."))