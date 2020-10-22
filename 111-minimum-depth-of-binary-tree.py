# 111. Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from
# the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5


# Constraints:
# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from utils import TreeNode, checkValue, treeFromArray


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, depth: int):
            if not node.left and not node.right:
                return depth
            ld = rd = float("inf")
            if node.left:
                ld = dfs(node.left, depth + 1)
            if node.right:
                rd = dfs(node.right, depth + 1)
            return min(ld, rd)

        if not root:
            return 0
        return dfs(root, 1)


t = Solution()

checkValue(2, t.minDepth(treeFromArray([3, 9, 20, None, None, 15, 7], 0)))
checkValue(1, t.minDepth(treeFromArray([2], 0)))
checkValue(0, t.minDepth(treeFromArray([], 0)))
