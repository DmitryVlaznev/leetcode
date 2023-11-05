# 501. Find Mode in Binary Search Tree

# Easy

# Given the root of a binary search tree (BST) with duplicates, return
# all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or
# equal to the node's key. The right subtree of a node contains only
# nodes with keys greater than or equal to the node's key. Both the left
# and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [1,null,2,2]
# Output: [2]

# Example 2:
# Input: root = [0]
# Output: [0]

# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5

# Follow up: Could you do that without using any extra space? (Assume
# that the implicit stack space incurred due to recursion does not
# count).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        from collections import deque, defaultdict

        dq, f = deque(), defaultdict(lambda: 0)
        dq.append(root)
        while dq:
            l = len(dq)
            while l:
                node = dq.popleft()
                f[node.val] += 1
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                l -= 1
        res, mf = [], -1
        for n, f in f.items():
            if f > mf:
                res, mf = [n], f
            elif f == mf:
                res.append(n)
        return res
