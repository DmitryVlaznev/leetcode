# 865. Smallest Subtree with all the Deepest Nodes

# Medium

# Given the root of a binary tree, the depth of each node is the
# shortest distance to the root.
# Return the smallest subtree such that it contains all the deepest
# nodes in the original tree.
# A node is called the deepest if it has the largest depth possible
# among any node in the entire tree.
# The subtree of a node is tree consisting of that node, plus the set of
# all descendants of that node.
# Note: This question is the same as 1123:
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/


# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the
# diagram. The nodes coloured in blue are the deepest nodes of the tree.
# Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but
# node 2 is the smallest subtree among them, so we return it.

# Example 2:
# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree.

# Example 3:
# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest node in the tree is 2, the valid subtrees are
# the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the
# smallest.

# Constraints:
# The number of nodes in the tree will be in the range [1, 500].
# 0 <= Node.val <= 500
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