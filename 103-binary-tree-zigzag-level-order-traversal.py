# 103. Binary Tree Zigzag Level Order Traversal

# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def fromArray(nodes: List[int], i: int) -> TreeNode:
        l = len(nodes)
        if not l: return None
        node = TreeNode(nodes[i])
        ch_i = 2 * i + 1
        node.left = Solution.fromArray(nodes, ch_i) if ch_i < l and nodes[ch_i] != None else None
        ch_i += 1
        node.right = Solution.fromArray(nodes, ch_i) if ch_i< l and nodes[ch_i] != None else None
        return node

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        from collections import deque
        dq = deque()
        res = []
        dq.append((0, root,))
        while dq:
            level, node = dq.popleft()
            if len(res) <= level: res.append([])
            res[level].append(node.val)
            if node.left: dq.append((level + 1, node.left))
            if node.right: dq.append((level + 1, node.right))

        for i, row in enumerate(res):
            if i % 2: row.reverse()
        return res

t = Solution()
print(t.zigzagLevelOrder(t.fromArray([3,9,20,None,None,15,7], 0)))
print(t.zigzagLevelOrder(t.fromArray([3,None,20], 0)))
print(t.zigzagLevelOrder(t.fromArray([3], 0)))
print(t.zigzagLevelOrder(t.fromArray([], 0)))