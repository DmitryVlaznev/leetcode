# 513. Find Bottom Left Tree Value

# Medium

# Given the root of a binary tree, return the leftmost value in the last
# row of the tree.


# Example 1:
# Input: root = [2,1,3]
# Output: 1

# Example 2:
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7


# Constraints:

# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        res = None

        dq.append(root)
        while dq:
            l = len(dq)
            res = dq[0].val
            while l:
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                l -= 1
        return res
