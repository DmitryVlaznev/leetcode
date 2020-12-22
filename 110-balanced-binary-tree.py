# 110. Balanced Binary Tree

# Easy

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node
# differ in height by no more than 1.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

from typing import Tuple
from utils import TreeNode, treeFromArray, checkValue


class Solution:
    def getSubtreeHeight(self, root: TreeNode) -> Tuple[int, bool]:
        if not root:
            return 0, True
        left_height, left_balanced = self.getSubtreeHeight(root.left)
        right_height, right_balanced = self.getSubtreeHeight(root.right)
        return (
            max(left_height, right_height) + 1,
            left_balanced and right_balanced and abs(left_height - right_height) < 2,
        )

    def isBalanced(self, root: TreeNode) -> bool:
        return self.getSubtreeHeight(root)[1]


t = Solution()

checkValue(True, t.isBalanced(treeFromArray([3, 9, 20, None, None, 15, 7], 0)))
checkValue(False, t.isBalanced(treeFromArray([1, 2, 2, 3, 3, None, None, 4, 4], 0)))
checkValue(True, t.isBalanced(None))
checkValue(True, t.isBalanced(treeFromArray([1], 0)))
