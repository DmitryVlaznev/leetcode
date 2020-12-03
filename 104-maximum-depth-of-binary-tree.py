# 104. Maximum Depth of Binary Tree

# Easy

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest
# path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Example 3:
# Input: root = []
# Output: 0

# Example 4:
# Input: root = [0]
# Output: 1


# Constraints:
# * The number of nodes in the tree is in the range [0, 104].
# * -100 <= Node.val <= 100


from utils import treeFromArray, checkValue, TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return (
            0
            if not root
            else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        )


t = Solution()

checkValue(3, t.maxDepth(treeFromArray([3, 9, 20, None, None, 15, 7], 0)))
checkValue(2, t.maxDepth(treeFromArray([3, None, 7], 0)))
checkValue(1, t.maxDepth(treeFromArray([3], 0)))
checkValue(1, t.maxDepth(treeFromArray([0], 0)))
checkValue(0, t.maxDepth(None))
