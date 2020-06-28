# 222. Count Complete Tree Nodes
# Given a complete binary tree, count the number of nodes.

# Note:

# Definition of a complete binary tree from Wikipedia:

# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2h nodes inclusive at the last
# level h.

# Example:
# Input:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# Output: 6

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

    def countBranchDepth(self, root: TreeNode, left=True) -> int:
        if not root:
            return 0
        d = 1
        n = root
        if left:
            while n.left:
                d += 1
                n = n.left
        else:
            while n.right:
                n = n.right
                d += 1
        return d

    def countSubTree(self, root: TreeNode, leftDepth: int, rightDepth: int) -> int:
        if not root: return 0

        ld, rd = leftDepth, rightDepth
        if ld is None: ld = self.countBranchDepth(root, True)
        if rd is None: rd = self.countBranchDepth(root, False)
        if ld == rd: return 2 ** ld - 1
        return (
            self.countSubTree(root.left, ld - 1, None)
            + self.countSubTree(root.right, None, rd - 1)
            + 1
        )

    def countNodes(self, root: TreeNode) -> int:
        return self.countSubTree(root, None, None)

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log(0, t.countNodes(t.fromArray([], 0)))
log(1, t.countNodes(t.fromArray([1,], 0)))
log(2, t.countNodes(t.fromArray([1,2,], 0)))
log(3, t.countNodes(t.fromArray([1,2,3], 0)))
log(4, t.countNodes(t.fromArray([1,2,3,4], 0)))
log(5, t.countNodes(t.fromArray([1,2,3,4,5], 0)))
log(6, t.countNodes(t.fromArray([1,2,3,4,5,6], 0)))
log(7, t.countNodes(t.fromArray([1,2,3,4,5,6,7], 0)))
log(8, t.countNodes(t.fromArray([1,2,3,4,5,6,7,8], 0)))