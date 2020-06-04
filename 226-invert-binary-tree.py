# 226. Invert Binary Tree

# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:

# Google: 90% of our engineers use the software you wrote (Homebrew),
# but you can’t invert a binary tree on a whiteboard so f*** off.

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def toArray(root: TreeNode) -> List[int]:
        if not root: return []
        def preorder(node: TreeNode, depth: int, traversal: List[List[int]]):
            while len(traversal) <= depth: traversal.append([])
            if node:
                traversal[depth].append(node.val)
                traversal = preorder(node.left, depth + 1, traversal)
                traversal = preorder(node.right, depth + 1, traversal)
            else:
                traversal[depth].append(None)
            return traversal
        res = [item for sublist in preorder(root, 0, []) for item in sublist]
        while res[-1] == None: res.pop()
        return res

    @staticmethod
    def fromArray(nodes: List[int], i: int) -> TreeNode:
        l = len(nodes)
        node = TreeNode(nodes[i])
        ch_i = 2 * i + 1
        node.left = Solution.fromArray(nodes, ch_i) if ch_i < l and nodes[ch_i] != None else None
        ch_i += 1
        node.right = Solution.fromArray(nodes, ch_i) if ch_i< l and nodes[ch_i] != None else None
        return node

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.right, root.left = root.left, root.right
            self.invertTree(root.left)
            self.invertTree(root.right)

        return root


def log(correct, res):
    if len(correct) == len(res) and set(correct) == set(res): print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log([3,20,9,7,15], t.toArray(t.invertTree(t.fromArray([3,9,20,None,None,15,7], 0))))
log([4,7,2,9,6,3,1], t.toArray(t.invertTree(t.fromArray([4,2,7,1,3,6,9], 0))))
