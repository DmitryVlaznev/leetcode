# 314. Binary Tree Vertical Order Traversal
# Medium

# Given the root of a binary tree, return the vertical order traversal
# of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from
# left to right.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]

# Example 2:
# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]

# Example 3:
# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# pylint: disable-all

from typing import Optional, List
from collections import defaultdict, deque
from utils import TreeNode


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dd = defaultdict(list)
        dq = deque()
        dq.append((root, 0))

        while dq:
            l = len(dq)
            while l:
                node, idx = dq.popleft()
                dd[idx].append(node.val)
                if node.left:
                    dq.append((node.left, idx - 1))
                if node.right:
                    dq.append((node.right, idx + 1))
                l -= 1

        indices = sorted(dd.keys())
        res = []
        for i in indices:
            res.append(dd[i])
        return res
