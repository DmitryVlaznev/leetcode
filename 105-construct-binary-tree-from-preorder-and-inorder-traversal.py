# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Medium

# Given two integer arrays preorder and inorder where preorder is the
# preorder traversal of a binary tree and inorder is the inorder
# traversal of the same tree, construct and return the binary tree.

# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.


from typing import List
from utils import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def add_node(
            preorder: List[int],
            pl: int,
            pr: int,
            inorder: List[int],
            il: int,
            ir: int,
        ):
            node = TreeNode(preorder[pl])
            if pl == pr:
                return node

            node_i = inorder.index(preorder[pl], il, ir + 1)
            if node_i > il:  # has left branch
                l_count = node_i - il
                node.left = add_node(
                    preorder, pl + 1, pl + l_count, inorder, il, node_i - 1
                )
            if node_i < ir:  # has right branch
                r_count = ir - node_i
                node.right = add_node(
                    preorder, pr - r_count + 1, pr, inorder, node_i + 1, ir
                )
            return node

        return add_node(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


t = Solution()
# t.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
t.buildTree([1, 2], [2, 1])
