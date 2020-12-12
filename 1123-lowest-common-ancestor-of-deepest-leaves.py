# 1123. Lowest Common Ancestor of Deepest Leaves

# Medium

# Given the root of a binary tree, return the lowest common ancestor of
# its deepest leaves.

# Recall that:

# The node of a binary tree is a leaf if and only if it has no children

# The depth of the root of the tree is 0. if the depth of a node is d,
# the depth of each of its children is d + 1.

# The lowest common ancestor of a set S of nodes, is the node A with the
# largest depth such that every node in S is in the subtree with root A.

# Note: This question is the same as 865:
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the diagram.
# The nodes coloured in blue are the deepest leaf-nodes of the tree.
# Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.

# Example 2:
# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree, and it's the lca of itself.

# Example 3:
# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.

# Constraints:
# The number of nodes in the tree will be in the range [1, 1000].
# 0 <= Node.val <= 1000
# The values of the nodes in the tree are unique.

from utils import TreeNode, treeFromArray, checkValue


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        from collections import deque

        dq = deque()
        dq.append((root, [root.val]))
        deepest = []
        while dq:
            level_nodes_count, deepest = len(dq), []
            while level_nodes_count:
                node, path = dq.popleft()
                deepest.append(path[:])
                if node.left:
                    dq.append((node.left, path[:] + [node.left.val]))
                if node.right:
                    dq.append((node.right, path[:] + [node.right.val]))
                level_nodes_count -= 1
        parents, subtree_path, p = set(), [], len(deepest[0])
        while len(parents) != 1:
            p -= 1
            parents.clear()
            for path in deepest:
                parents.add(path[p])
        subtree_path = deepest[0][0 : p + 1]

        node = root
        for v in subtree_path[1:]:
            if node.left and node.left.val == v:
                node = node.left
            else:
                node = node.right
        return node


t = Solution()

root = treeFromArray([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 0)
checkValue(2, t.subtreeWithAllDeepest(root).val)

root = treeFromArray([1], 0)
checkValue(1, t.subtreeWithAllDeepest(root).val)

root = treeFromArray([0, 1, 3, None, 2], 0)
checkValue(2, t.subtreeWithAllDeepest(root).val)