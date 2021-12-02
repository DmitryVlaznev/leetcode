# 333. Largest BST Subtree

# Medium

# Given the root of a binary tree, find the largest subtree, which is
# also a Binary Search Tree (BST), where the largest means subtree has
# the largest number of nodes.

# A Binary Search Tree (BST) is a tree in which all the nodes follow the
# below-mentioned properties:

# The left subtree values are less than the value of their parent (root) node's value.
# The right subtree values are greater than the value of their parent (root) node's value.
# Note: A subtree must include all of its descendants.


# Example 1:
# Input: root = [10,5,15,1,8,null,7]
# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted
# one. The return value is the subtree's size, which is 3.

# Example 2:
# Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -10^4 <= Node.val <= 10^4

# Follow up: Can you figure out ways to solve it with O(n) time complexity?

from typing import Optional
from utils import TreeNode, treeFromArray, checkValue


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal res

            if not node:
                return True, float("inf"), float("-inf"), 0

            left_is_bst, left_min, left_max, left_nodes = dfs(node.left)
            right_is_bst, right_min, right_max, right_nodes = dfs(node.right)

            if left_is_bst and right_is_bst:
                if node.left and left_max >= node.val:
                    return False, float("inf"), float("-inf"), 0
                if node.right and right_min <= node.val:
                    return False, float("inf"), float("-inf"), 0

                subtree_size = 1 + left_nodes + right_nodes
                res = max(res, subtree_size)

                return (
                    True,
                    min(left_min, right_min, node.val),
                    max(left_max, right_max, node.val),
                    subtree_size,
                )
            return False, float("inf"), float("-inf"), 0

        dfs(root)
        return res


s = Solution()
checkValue(3, s.largestBSTSubtree(treeFromArray([10, 5, 15, 1, 8, None, 7], 0)))
checkValue(2, s.largestBSTSubtree(treeFromArray([3, 2, 4, None, None, 1], 0)))
