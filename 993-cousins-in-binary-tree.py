# 993. Cousins in Binary Tree

# In a binary tree, the root node is at depth 0, and children of each
# depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth,
# but have different parents.

# We are given the root of a binary tree with unique values, and the
# values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and
# y are cousins.

# Example 1:
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false

# Example 2:
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true

# Example 3:
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false


# Note:
# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.

# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def fromArray(nodes: List[int], i: int) -> TreeNode:
        l = len(nodes)
        node = TreeNode(nodes[i])
        ch_i = 2 * i + 1
        node.left = Solution.fromArray(nodes, ch_i) if ch_i < l and nodes[ch_i] != None else None
        ch_i += 1
        node.right = Solution.fromArray(nodes, ch_i) if ch_i< l and nodes[ch_i] != None else None
        return node

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        from collections import deque
        x_data = None
        y_data = None
        queue = deque()
        queue.append({"parent": None, "node": root, "level": 0})

        while not x_data or not y_data:
            item = queue.popleft()
            if item["node"].val == x: x_data = item
            if item["node"].val == y: y_data = item
            if item["node"].left:
                queue.append({"parent": item["node"], "node": item["node"].left, "level": item["level"] + 1})
            if item["node"].right:
                queue.append({"parent": item["node"], "node": item["node"].right, "level": item["level"] + 1})
        # print("x_data", x_data)
        # print("y_data", y_data)
        return x_data["level"] == y_data["level"] and x_data["parent"] != y_data["parent"]

t = Solution()
print("False", t.isCousins(t.fromArray([1,2,3,4], 0), 4, 3))
print("True", t.isCousins(t.fromArray([1,2,3,None,4,None,5], 0), 5, 4))
print("False", t.isCousins(t.fromArray([1,2,3,None,4], 0), 2, 3))
print("False", t.isCousins(t.fromArray([1,2], 0), 1, 2))