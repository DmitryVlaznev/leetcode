# 653. Two Sum IV - Input is a BST

# Easy

# Given the root of a Binary Search Tree and a target number k, return
# true if there exist two elements in the BST such that their sum is
# equal to the given target.

# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Example 2:
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false

# Example 3:
# Input: root = [2,1,3], k = 4
# Output: true

# Example 4:
# Input: root = [2,1,3], k = 1
# Output: false

# Example 5:
# Input: root = [2,1,3], k = 3
# Output: true

# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -10^4 <= Node.val <= 10^4
# root is guaranteed to be a valid binary search tree.
# -10^5 <= k <= 10^5

from typing import Optional
from utils import TreeNode
from collections import deque


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        seen, dq = set(), deque()
        dq.append(root)
        while dq:
            l = len(dq)
            while l:
                l -= 1
                node = dq.popleft()
                if node.val in seen:
                    return True
                seen.add(k - node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return False
