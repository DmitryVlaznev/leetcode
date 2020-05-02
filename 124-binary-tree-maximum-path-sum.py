# 124. Binary Tree Maximum Path Sum

# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child
# connections. The path must contain at least one node and does not need
# to go through the root.

# Example 1:
# Input: [1,2,3]
#        1
#       / \
#      2   3
# Output: 6

# Example 2:
# Input: [-10,9,20,null,null,15,7]
#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42

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
        node.left = Solution.fromArray(nodes, ch_i) if ch_i < l and nodes[i] != None else None
        ch_i += 1
        node.right = Solution.fromArray(nodes, ch_i) if ch_i< l and nodes[i] != None else None
        return node

    path_sum = None

    def update_max_path(self, node_val, left_val, right_val):
        mp = max(node_val, node_val + left_val, node_val + right_val, node_val + left_val + right_val)
        self.path_sum = max(self.path_sum, mp)

    def max_path(self, root: TreeNode) -> int:
        if root.val is None: return 0
        lp = self.max_path(root.left) if root.left is not None else 0
        rp = self.max_path(root.right) if root.right is not None else 0
        max_branch_path = max(lp, rp)
        max_node_path = max(root.val, max_branch_path + root.val)
        self.update_max_path(root.val, lp, rp)
        return max_node_path

    def maxPathSum(self, root: TreeNode) -> int:
        if not root or root.val is None: return 0
        self.path_sum = float("-inf")
        lp = self.max_path(root.left) if root.left is not None else 0
        rp = self.max_path(root.right) if root.right is not None else 0
        self.update_max_path(root.val, lp, rp)
        return self.path_sum

t = Solution()

tree = t.fromArray([1,2,3], 0)
print("6 = ", t.maxPathSum(tree))

tree = t.fromArray([-10,9,20,None,None,15,7], 0)
print("42 = ", t.maxPathSum(tree))

tree = t.fromArray([1], 0)
print("1 = ", t.maxPathSum(tree))

print("0 = ", t.maxPathSum(None))

tree = t.fromArray([1, 2], 0)
print("3 = ", t.maxPathSum(tree))

tree = t.fromArray([1, 2, 3, None, None, 6, 7, None, None, None, None, 12, None, None, 15, None, None, None, None, None, None, None, None, 24, None, None, None, None, None, None, 31], 0)
print("98 = ", t.maxPathSum(tree))

tree = t.fromArray([-3], 0)
print("-3 = ", t.maxPathSum(tree))

tree = t.fromArray([-1,-2,-3], 0)
print("-1 = ", t.maxPathSum(tree))

tree = t.fromArray([2,-1], 0)
print("2 = ", t.maxPathSum(tree))



