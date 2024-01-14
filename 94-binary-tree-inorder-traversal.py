# 94. Binary Tree Inorder Traversal

# Solved

# Given the root of a binary tree, return the inorder traversal of its
# nodes' values.


# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]


# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack, res, visited = [root], [], set()
        while stack:
            node = stack.pop()
            if node.left and node.left not in visited:
                stack.append(node)
                stack.append(node.left)
            else:
                res.append(node.val)
                visited.add(node)
                if node.right:
                    stack.append(node.right)
        return res
