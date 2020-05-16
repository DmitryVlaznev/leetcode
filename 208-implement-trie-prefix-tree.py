# 208. Implement Trie (Prefix Tree)
# Implement a trie with insert, search, and startsWith methods.

# Example:
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
# Note:

# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.

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

trie = Trie()
print("False", trie.search("wre"))
trie.insert("apple")
print("True", trie.search("apple"))
print("False", trie.search("app"))
print("True", trie.startsWith("app"))
trie.insert("app")
print("True", trie.search("app"))