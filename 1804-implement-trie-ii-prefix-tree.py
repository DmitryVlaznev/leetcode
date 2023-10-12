# 1804. Implement Trie II (Prefix Tree)

# Medium

# A trie (pronounced as "try") or prefix tree is a tree data structure
# used to efficiently store and retrieve keys in a dataset of strings.
# There are various applications of this data structure, such as
# autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
#  * void insert(String word) Inserts the string word into the trie.
#  * int countWordsEqualTo(String word) Returns the number of instances
#    of the string word in the trie.
#  * int countWordsStartingWith(String prefix) Returns the number of
#    strings in the trie that have the string prefix as a prefix.
#  * void erase(String word) Erases the string word from the trie.


# Example 1:
# Input
# ["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
# [[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
# Output
# [null, null, null, 2, 2, null, 1, 1, null, 0]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");               // Inserts "apple".
# trie.insert("apple");               // Inserts another "apple".
# trie.countWordsEqualTo("apple");    // There are two instances of "apple" so return 2.
# trie.countWordsStartingWith("app"); // "app" is a prefix of "apple" so return 2.
# trie.erase("apple");                // Erases one "apple".
# trie.countWordsEqualTo("apple");    // Now there is only one instance of "apple" so return 1.
# trie.countWordsStartingWith("app"); // return 1
# trie.erase("apple");                // Erases "apple". Now the trie is empty.
# trie.countWordsStartingWith("app"); // return 0


# Constraints:

# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, countWordsEqualTo, countWordsStartingWith, and erase.
# It is guaranteed that for any function call to erase, the string word will exist in the trie.


class Trie:
    def __init__(self):
        self.root = {"children": {}}

    def insert(self, word: str) -> None:
        node = self.root
        for l in word:
            if not l in node["children"]:
                node["children"][l] = {"words": 0, "prefix": 0, "children": {}}
            node["children"][l]["prefix"] += 1
            node = node["children"][l]
        node["words"] += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for l in word:
            if not l in node["children"]:
                return 0
            node = node["children"][l]
        return node["words"]

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for l in prefix:
            if not l in node["children"]:
                return 0
            node = node["children"][l]
        return node["prefix"]

    def erase(self, word: str) -> None:
        node = self.root
        for l in word:
            t = node["children"][l]
            node["children"][l]["prefix"] -= 1
            if node["children"][l]["prefix"] == 0:
                del node["children"][l]
            node = t
        node["words"] -= 1


from utils import checkValue

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
trie.insert("apple")
checkValue(2, trie.countWordsEqualTo("apple"))
checkValue(2, trie.countWordsStartingWith("app"))
trie.erase("apple")
checkValue(1, trie.countWordsEqualTo("apple"))
checkValue(1, trie.countWordsStartingWith("app"))
trie.erase("apple")
checkValue(0, trie.countWordsStartingWith("app"))