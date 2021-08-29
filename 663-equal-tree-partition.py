# 663. Equal Tree Partition

# Medium

# Given the root of a binary tree, return true if you can partition the
# tree into two trees with equal sums of values after removing exactly
# one edge on the original tree.

# Example 1:
# Input: root = [5,10,10,null,null,2,3]
# Output: true

# Example 2:
# Input: root = [1,2,10,null,null,2,20]
# Output: false
# Explanation: You cannot split the tree into two trees with equal sums
# after removing exactly one edge on the tree.

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -10^5 <= Node.val <= 10^5

from typing import Optional
from utils import TreeNode
from functools import lru_cache
from collections import deque


class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        @lru_cache(maxsize=None)
        def subtree_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return node.val + subtree_sum(node.left) + subtree_sum(node.right)

        total = subtree_sum(root)
        dq = deque()
        if root.left:
            dq.append(root.left)
        if root.right:
            dq.append(root.right)
        while dq:
            l = len(dq)
            while l:
                l -= 1
                node = dq.popleft()
                node_sum = subtree_sum(node)
                if total - node_sum == node_sum:
                    return True
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return False
