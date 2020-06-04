# 102. Binary Tree Level Order Traversal

# Given a binary tree, return the level order traversal of its nodes'
# values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def fromArray(nodes: List[int], i: int) -> TreeNode:
        l = len(nodes)
        if not l: return None
        node = TreeNode(nodes[i])
        ch_i = 2 * i + 1
        node.left = Solution.fromArray(nodes, ch_i) if ch_i < l and nodes[ch_i] != None else None
        ch_i += 1
        node.right = Solution.fromArray(nodes, ch_i) if ch_i< l and nodes[ch_i] != None else None
        return node

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        def preorder(node: TreeNode, depth: int, traversal: List[List[int]]):
            while len(traversal) <= depth: traversal.append([])
            if node.val != None: traversal[depth].append(node.val)
            if node.left != None: traversal = preorder(node.left, depth + 1, traversal)
            if node.right != None: traversal = preorder(node.right, depth + 1, traversal)
            return traversal

        return preorder(root, 0, [])

t = Solution()

print(t.levelOrder(t.fromArray([3,9,20,None,None,15,7], 0)))
print(t.levelOrder(t.fromArray([], 0)))