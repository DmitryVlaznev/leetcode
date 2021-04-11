# 1302. Deepest Leaves Sum

# Given the root of a binary tree, return the sum of values of its
# deepest leaves.

# Example 1:
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15

# Example 2:
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19


# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 100

from utils import TreeNode


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res, deepest = 0, 0

        def dfs(node: TreeNode, deep: int):
            nonlocal res, deepest

            if not node:
                return

            dfs(node.left, deep + 1)
            if not node.left and not node.right:
                if deep > deepest:
                    deepest = deep
                    res = 0
                if deep == deepest:
                    res += node.val
            dfs(node.right, deep + 1)

        dfs(root, 1)
        return res