# 988. Smallest String Starting From Leaf

# Medium

# You are given the root of a binary tree where each node has a value in
# the range [0, 25] representing the letters 'a' to 'z'.

# Return the lexicographically smallest string that starts at a leaf of
# this tree and ends at the root.

# As a reminder, any shorter prefix of a string is lexicographically
# smaller.

# For example, "ab" is lexicographically smaller than "aba".
# A leaf of a node is a node that has no children.


# Example 1:
# Input: root = [0,1,2,3,4,3,4]
# Output: "dba"

# Example 2:
# Input: root = [25,1,3,1,3,0,2]
# Output: "adz"

# Example 3:
# Input: root = [2,2,1,null,1,0,null,0]
# Output: "abc"


# Constraints:

# The number of nodes in the tree is in the range [1, 8500].
# 0 <= Node.val <= 25


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Trie:
    def __init__(self):
        self.root = {"leaf": False, "children": [None] * 26}

    def insert(self, arr: List[int]) -> None:
        node = self.root
        for val in arr:
            if node["children"][val] is None:
                node["children"][val] = {"leaf": False, "children": [None] * 26}
            node = node["children"][val]
        node["leaf"] = True

    def get_smallest_seq(self):
        res = []
        node = self.root
        while True:
            for i in range(26):
                if node["children"][i] != None:
                    res.append(i)
                    if node["children"][i]["leaf"]:
                        return res
                    node = node["children"][i]
                    break

    def get_smallest_string(self):
        return "".join([chr(ord("a") + i) for i in self.get_smallest_seq()])


class Solution2:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        trie = Trie()

        def dfs(node, path):
            path.append(node.val)
            if node.left == None and node.right == None:
                trie.insert(path[::-1])
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return trie.get_smallest_string()


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = chr(ord("z") + 1)

        def dfs(node, path):
            nonlocal res
            path.append(node.val)
            if node.left == None and node.right == None:
                cand = "".join([chr(ord("a") + i) for i in path[::-1]])
                res = min(res, cand)
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return res
