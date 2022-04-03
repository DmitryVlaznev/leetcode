# 236. Lowest Common Ancestor of a Binary Tree

# Given a binary tree, find the lowest common ancestor (LCA) of two
# given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common
# ancestor is defined between two nodes p and q as the lowest node in T
# that has both p and q as descendants (where we allow a node to be a
# descendant of itself).”


# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a
# descendant of itself according to the LCA definition.

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1


# Constraints:
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

from utils import TreeNode
from typing import List


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        p_path, q_path = None, None

        def dfs(path):
            nonlocal p_path, q_path
            if path[-1] == p:
                p_path = path[:]
            elif path[-1] == q:
                q_path = path[:]
            if p_path and q_path:
                return
            if path[-1].left:
                path.append(path[-1].left)
                dfs(path)
                path.pop()
            if path[-1].right:
                path.append(path[-1].right)
                dfs(path)
                path.pop()

        dfs([root])
        res = None
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] == q_path[i]:
                res = p_path[i]
            else:
                break
        return res
