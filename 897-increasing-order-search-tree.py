# 897. Increasing Order Search Tree

# Easy

# Given the root of a binary search tree, rearrange the tree in in-order
# so that the leftmost node in the tree is now the root of the tree, and
# every node has no left child and only one right child.

# Example 1:
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

# Example 2:
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]

# Constraints:

# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000

from utils import TreeNode, treeFromArray, checkList


class Solution:
    def inorder(self, node: TreeNode) -> TreeNode:
        if not node:
            return None, None
        lh, lt = self.inorder(node.left)
        rh, rt = self.inorder(node.right)

        head = lh
        if head:
            lt.right = node
        else:
            head = node
        if rh:
            node.right = rh
            tail = rt
        else:
            tail = node
        node.left = None
        return head, tail

    def increasingBST(self, root: TreeNode) -> TreeNode:
        head, tail = self.inorder(root)
        return head


from typing import List


def treeToList(root: TreeNode) -> List[int]:
    res = []
    p = root
    while p:
        res.append(p.val)
        p = p.right
    return res


t = Solution()

head = t.increasingBST(
    treeFromArray([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9], 0)
)
checkList(
    [1, 2, 3, 4, 5, 6, 8],
    treeToList(head),
)

head = t.increasingBST(treeFromArray([5, 1, 7], 0))
checkList(
    [1, 5, 7],
    treeToList(head),
)
