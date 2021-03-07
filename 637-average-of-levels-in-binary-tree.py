# 637. Average of Levels in Binary Tree

# Easy

# Given a non-empty binary tree, return the average value of the nodes
# on each level in the form of an array.

# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and
# on level 2 is 11. Hence return [3, 14.5, 11].

# Note:
# The range of node's value is in the range of 32-bit signed integer.

from typing import List
from utils import TreeNode
from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res, dq = [], deque()
        dq.append(root)
        while dq:
            levelSize = rest = len(dq)
            levelAverage = 0.0
            while rest:
                rest -= 1
                node = dq.popleft()
                levelAverage += node.val / levelSize
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(levelAverage)
        return res

    def averageOfLevels2(self, root: TreeNode) -> List[float]:
        res, dq = [], deque()
        dq.append(root)
        while dq:
            levelSize = rest = len(dq)
            s = 0.0
            while rest:
                rest -= 1
                node = dq.popleft()
                s += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(s / levelSize)
        return res
