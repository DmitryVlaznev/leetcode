# 101. Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of
# itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100

# Follow up: Could you solve it both recursively and iteratively?

from utils import TreeNode, treeFromArray
from typing import Optional
from collections import deque


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkNodes(a: Optional[TreeNode], b: Optional[TreeNode]):
            if a is None and b is None:
                return True

            if a is None or b is None:
                return False

            return (
                a.val == b.val
                and checkNodes(a.left, b.right)
                and checkNodes(a.right, b.left)
            )

        if not root:
            return True

        return checkNodes(root.left, root.right)


s = Solution()
s.isSymmetric(treeFromArray([1, 2, 2, 3, 4, 4, 3], 0))
