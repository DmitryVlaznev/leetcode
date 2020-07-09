# 662. Maximum Width of Binary Tree

# Given a binary tree, write a function to get the maximum width of the
# given tree. The width of a tree is the maximum width among all levels.
# The binary tree has the same structure as a full binary tree, but some
# nodes are null.

# The width of one level is defined as the length between the end-nodes
# (the leftmost and right most non-null nodes in the level, where the
# null nodes between the end-nodes are also counted into the length
# calculation.

# Example 1:
# Input:
#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9
# Output: 4
# Explanation: The maximum width existing in the third level with the
# length 4 (5,3,null,9).

# Example 2:
# Input:
#           1
#          /
#         3
#        / \
#       5   3
# Output: 2
# Explanation: The maximum width existing in the third level with the
# length 2 (5,3).

# Example 3:
# Input:
#           1
#          / \
#         3   2
#        /
#       5
# Output: 2
# Explanation: The maximum width existing in the second level with the
# length 2 (3,2).

# Example 4:
# Input:
#           1
#          / \
#         3   2
#        /     \
#       5       9
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the
# length 8 (6,null,null,null,null,null,null,7).

# Note: Answer will in the range of 32-bit signed integer.

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

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0

        from collections import deque
        q = deque()
        q.append([0, root])
        res = 0
        while q:
            level_count = len(q)
            l = r = None
            for i in range(level_count):
                idx, node = q.popleft()
                if not l: l = r = idx
                r = max(r, idx)
                if node.left: q.append([idx * 2 + 1, node.left])
                if node.right: q.append([idx * 2 + 2, node.right])
            res = max(res, r - l + 1)
        return res



def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

tree = [1,3,2,5,3,None,9]
log(4, t.widthOfBinaryTree(t.fromArray(tree, 0)))

tree = [1,3,None,5,3]
log(2, t.widthOfBinaryTree(t.fromArray(tree, 0)))

tree = [1,3]
log(1, t.widthOfBinaryTree(t.fromArray(tree, 0)))

tree = [1]
log(1, t.widthOfBinaryTree(t.fromArray(tree, 0)))

tree = []
log(0, t.widthOfBinaryTree(t.fromArray(tree, 0)))

tree = [1,3,2,5]
log(2, t.widthOfBinaryTree(t.fromArray(tree, 0)))

tree = [1,3,2,5,None,None,9,6,None,None,None,None,None,None,7]
log(8, t.widthOfBinaryTree(t.fromArray(tree, 0)))