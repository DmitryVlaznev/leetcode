# 1120. Maximum Average Subtree

# Medium

# Given the root of a binary tree, return the maximum average value of a
# subtree of that tree. Answers within 10^-5 of the actual answer will be
# accepted.

# A subtree of a tree is any node of that tree plus all its descendants.

# The average value of a tree is the sum of its values, divided by the
# number of nodes.

# Example 1:
# Input: root = [5,6,1]
# Output: 6.00000
# Explanation:
# For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
# For the node with value = 6 we have an average of 6 / 1 = 6.
# For the node with value = 1 we have an average of 1 / 1 = 1.
# So the answer is 6 which is the maximum.

# Example 2:
# Input: root = [0,null,1]
# Output: 1.00000

# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^5

from typing import Optional
from utils import TreeNode
from functools import lru_cache


class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = 0

        @lru_cache(maxsize=None)
        def subtree_average(node):
            nonlocal res
            if not node:
                return 0, 0
            left_nodes, left_sum = subtree_average(node.left)
            right_nodes, right_sum = subtree_average(node.right)
            avg = (node.val + left_sum + right_sum) / (1 + left_nodes + right_nodes)
            res = max(res, avg)
            return (1 + left_nodes + right_nodes), (node.val + left_sum + right_sum)

        subtree_average(root)
        return res
