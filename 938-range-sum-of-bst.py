# 938. Range Sum of BST

# Easy

# Given the root node of a binary search tree, return the sum of values
# of all nodes with a value in the range [low, high].

# Example 1:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32

# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23

# Constraints:
# The number of nodes in the tree is in the range [1, 2 * 104].
# 1 <= Node.val <= 105
# 1 <= low <= high <= 105
# All Node.val are unique.

from utils import TreeNode, treeFromArray, checkValue


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        if root.val >= low and root.val <= high:
            return (
                root.val
                + self.rangeSumBST(root.left, low, high)
                + self.rangeSumBST(root.right, low, high)
            )
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        else:
            # root.val > high:
            return self.rangeSumBST(root.left, low, high)
