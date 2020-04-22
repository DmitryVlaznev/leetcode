# 1008. Construct Binary Search Tree from Preorder Traversal

# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every
# node, any descendant of node.left has a value < node.val, and any
# descendant of node.right has a value > node.val.  Also recall that a
# preorder traversal displays the value of the node first, then
# traverses node.left, then traverses node.right.)

# Example 1:
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Note:
# 1 <= preorder.length <= 100
# The values of preorder are distinct.

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def subtree(self, preorder, start, end):
        if start == end:
            return TreeNode(preorder[start])

        v = preorder[start]
        left_i = start + 1 if preorder[start + 1] < v else None

        import bisect

        right_i = (
            bisect.bisect(preorder, v, start + 1, end) if preorder[end] > v else None
        )

        node = TreeNode(v)
        if left_i is not None:
            branch_end = right_i - 1 if right_i is not None else end
            node.left = self.subtree(preorder, left_i, branch_end)
        if right_i is not None:
            node.right = self.subtree(preorder, right_i, end)
        return node

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not len(preorder):
            return None
        return self.subtree(preorder, 0, len(preorder) - 1)

    # The approach below is O(n log n) instead of the above which is O(n)

    # def put(self, node, val):
    #     if not node: return TreeNode(val)
    #     if val < node.val: node.left = self.put(node.left, val)
    #     if val > node.val: node.right = self.put(node.right, val)
    #     return node

    # def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    #     if not len(preorder): return None
    #     root = None
    #     for v in preorder:
    #         root = self.put(root, v)
    #     return root


t = Solution()
# print(t.bstFromPreorder([8,5,1,7,10,12,11]))
print(t.bstFromPreorder([8, 5, 1]))

# if right_i is not None:
#     while preorder[right_i - 1] > v: right_i -= 1

# t = bisect.bisect(preorder, v, start + 1, end)

# print("t = ", t, "right_i = ", right_i, "v = ", v, "start = ", start, "end = ", end)
