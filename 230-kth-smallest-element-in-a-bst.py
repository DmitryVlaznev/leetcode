# 230. Kth Smallest Element in a BST

# Given a binary search tree, write a function kthSmallest to find the
# kth smallest element in it.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example 1:
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1

# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3

# Follow up:
# * What if the BST is modified (insert/delete operations) often and you
# * need to find the kth smallest frequently? How would you optimize the
# * kthSmallest routine?

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
        node = TreeNode(nodes[i])
        ch_i = 2 * i + 1
        node.left = Solution.fromArray(nodes, ch_i) if ch_i < l and nodes[ch_i] != None else None
        ch_i += 1
        node.right = Solution.fromArray(nodes, ch_i) if ch_i < l and nodes[ch_i] != None else None
        return node

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        p = root
        while k:
            if p:
                stack.append(p)
                p = p.left
            else :
                p = stack.pop()
                k -= 1
                if k == 0: return p.val
                p = p.right

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

# tree = t.fromArray([3,1,4,None,2], 0)
# log(3, tree.val)
# log(1, tree.left.val)
# log(None, tree.left.left)
# log(2, tree.left.right.val)
# log(None, tree.left.right.left)
# log(None, tree.left.right.right)
# log(4, tree.right.val)
# log(None, tree.right.left)
# log(None, tree.right.right)


log(1, t.kthSmallest(t.fromArray([3,1,4,None,2], 0), 1))
log(3, t.kthSmallest(t.fromArray([5,3,6,2,4,None,None,1], 0), 3))
log(4, t.kthSmallest(t.fromArray([5,3,6,2,4,None,None,1], 0), 4))
log(5, t.kthSmallest(t.fromArray([5], 0), 1))