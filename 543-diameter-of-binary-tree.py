# 543. Diameter of Binary Tree

# Given a binary tree, you need to compute the length of the diameter of
# the tree. The diameter of a binary tree is the length of the longest
# path between any two nodes in a tree. This path may or may not pass
# through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the
# number of edges between them.

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    @staticmethod
    def fromArray(nodes: List[int], i: int) -> TreeNode:
        l = len(nodes)
        node = TreeNode(nodes[i])
        ch_i = 2 * i + 1
        node.left = Solution.fromArray(nodes, ch_i) if ch_i < l and nodes[ch_i] != None else None
        ch_i += 1
        node.right = Solution.fromArray(nodes, ch_i) if ch_i< l and nodes[ch_i] != None else None
        return node

    diameter = None

    def max_depth(self, root: TreeNode) -> int:
        ld = self.max_depth(root.left) + 1 if root.left else 0
        rd = self.max_depth(root.right) + 1 if root.right else 0
        subtree_diameter = ld + rd
        self.diameter = max(self.diameter, subtree_diameter)
        return max(ld, rd)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        if not root: return 0
        ld = self.max_depth(root.left) + 1 if root.left else 0
        rd = self.max_depth(root.right) + 1 if root.right else 0
        return max(self.diameter, ld + rd)

t = Solution()
tree = t.fromArray([1,2,3,4,5], 0)
print("3 = ", t.diameterOfBinaryTree(tree))

tree = t.fromArray([1], 0)
print("0 = ", t.diameterOfBinaryTree(tree))

print("0 = ", t.diameterOfBinaryTree(None))

tree = t.fromArray([1, 2], 0)
print("1 = ", t.diameterOfBinaryTree(tree))

tree = t.fromArray([1, 2, 3], 0)
print("2 = ", t.diameterOfBinaryTree(tree))

tree = t.fromArray([1, 2, 3, None, None, 6, 7, None, None, None, None, 12, None, None, 15, None, None, None, None, None, None, None, None, 24, None, None, None, None, None, None, 31], 0)
print("6 = ", t.diameterOfBinaryTree(tree))
