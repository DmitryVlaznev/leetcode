# 98. Validate Binary Search Tree

# Medium

# Given the root of a binary tree, determine if it is a valid binary
# search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the
# node's key. The right subtree of a node contains only nodes with keys
# greater than the node's key. Both the left and right subtrees must
# also be binary search trees.

# Example 1:
# Input: root = [2,1,3]
# Output: true
# Example 2:

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is
# 4.


# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

from utils import TreeNode, checkValue, treeFromArray


class Solution:
    def isValidSubtree(self, root: TreeNode, max_val: int, min_val: int) -> bool:
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        left = self.isValidSubtree(root.left, min(max_val, root.val), min_val)
        right = self.isValidSubtree(root.right, max_val, max(min_val, root.val))
        return left and right

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidSubtree(root, float("inf"), float("-inf"))


t = Solution()

# checkValue(True, t.isValidBST(treeFromArray([2, 1, 3], 0)))
# checkValue(False, t.isValidBST(treeFromArray([5, 1, 4, None, None, 3, 6], 0)))
checkValue(False, t.isValidBST(treeFromArray([1, 1], 0)))
checkValue(False, t.isValidBST(treeFromArray([1, None, 1], 0)))
