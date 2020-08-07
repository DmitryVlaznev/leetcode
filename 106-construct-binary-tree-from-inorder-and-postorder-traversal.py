# 106. Construct Binary Tree from Inorder and Postorder Traversal

# Given inorder and postorder traversal of a tree, construct the binary
# tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def inorder(node: TreeNode, traversal: List[int]):
        if node is None: return traversal
        Solution.inorder(node.left, traversal)
        traversal.append(node.val)
        Solution.inorder(node.right, traversal)
        return traversal

    def getRootIndex(self, inorder: List[int], root_val):
        for i, v in enumerate(inorder):
            if v == root_val: return i

    def createSubtree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # print(f"createSubtree | inorder = {inorder}, postorder = {postorder}")
        if not len(inorder): return None
        root_val = postorder.pop()
        r_node = TreeNode(root_val)
        r_idx = self.getRootIndex(inorder, root_val)
        if r_idx > 0:
            r_node.left = self.createSubtree(inorder[:r_idx], postorder[:r_idx])
        if r_idx < len(inorder) - 1:
            r_node.right = self.createSubtree(inorder[r_idx + 1:], postorder[r_idx:])
        return r_node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.createSubtree(inorder, postorder)


def log(correct, res):
    if len(correct) == len(res) and "".join(str(s) for s in correct) == "".join(str(s) for s in res):
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log([9,3,15,20,7], t.inorder(t.buildTree([9,3,15,20,7], [9,15,7,20,3]), []))
log([4,2,5,1,6,3,7], t.inorder(t.buildTree([4,2,5,1,6,3,7], [4,5,2,6,7,3,1]), []))
log([3,15,20,7], t.inorder(t.buildTree([3,15,20,7], [15,7,20,3]), []))
log([3,2,4,1], t.inorder(t.buildTree([3,2,4,1], [3,4,2,1]), []))
log([3], t.inorder(t.buildTree([3], [3]), []))
log([], t.inorder(t.buildTree([], []), []))