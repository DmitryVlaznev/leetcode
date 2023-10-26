# 515. Find Largest Value in Each Tree Row

# Medium

# Given the root of a binary tree, return an array of the largest value
# in each row of the tree (0-indexed).


# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]

# Example 2:
# Input: root = [1,2,3]
# Output: [1,3]


# Constraints:
# The number of nodes in the tree will be in the range [0, 10^4].
# -2^31 <= Node.val <= 2^31 - 1

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        from collections import deque

        dq, res = deque(), []
        dq.append(root)
        while dq:
            l, row_max = len(dq), float("-inf")
            while l:
                node: TreeNode = dq.popleft()
                row_max = max(row_max, node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                l -= 1
            res.append(row_max)
        return res