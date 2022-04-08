# 572. Subtree of Another Tree

# Easy

# Given the roots of two binary trees root and subRoot, return true if
# there is a subtree of root with the same structure and node values of
# subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in
# tree and all of this node's descendants. The tree tree could also be
# considered as a subtree of itself.

# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# Constraints:
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4

from typing import Optional
from utils import TreeNode
from collections import deque


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(node1, node2):
            if node1 is None or node2 is None:
                return node1 == node2
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.left) and check(node1.right, node2.right)

        dq = deque()
        dq.append(root)
        while dq:
            l = len(dq)
            while l:
                l -= 1
                node = dq.popleft()
                if check(node, subRoot):
                    return True
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return False
