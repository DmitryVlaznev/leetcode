# 1026. Maximum Difference Between Node and Ancestor

# Given the root of a binary tree, find the maximum value V for which
# there exist different nodes A and B where V = |A.val - B.val| and A is
# an ancestor of B.

# A node A is an ancestor of B if either: any child of A is equal to B,
# or any child of A is an ancestor of B.

# Example 1:
# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

# Example 2:
# Input: root = [1,null,2,null,0,3]
# Output: 3


# Constraints:
# The number of nodes in the tree is in the range [2, 5000].
# 0 <= Node.val <= 105

from utils import TreeNode, treeFromArray, checkValue


class Solution:
    res = 0

    def findSubtreeMinMax(self, node: TreeNode, min_max):
        min_max[0] = min(min_max[0], node.val)
        min_max[1] = max(min_max[1], node.val)

        self.res = max(min_max[1] - min_max[0], self.res)

        if node.left:
            self.findSubtreeMinMax(node.left, min_max.copy())
        if node.right:
            self.findSubtreeMinMax(node.right, min_max.copy())

    def maxAncestorDiff(self, root: TreeNode) -> int:
        l, r = [root.val, root.val], [root.val, root.val]
        if root.left:
            self.findSubtreeMinMax(root.left, l)
        if root.right:
            self.findSubtreeMinMax(root.right, r)

        return self.res
