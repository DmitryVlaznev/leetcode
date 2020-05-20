# Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree

# Given a binary tree where each path going from the root to any leaf
# form a valid sequence, check if a given string is a valid sequence in
# such binary tree.

# We get the given string from the concatenation of an array of integers
# arr and the concatenation of all values of the nodes along a path
# results in a sequence in the given binary tree.

# Example 1:
# Input: root = [0,1,0,0,1,0,None,None,1,0,0], arr = [0,1,0,1]
# Output: true
# Explanation:
# The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
# Other valid sequences are:
# 0 -> 1 -> 1 -> 0
# 0 -> 0 -> 0

# Example 2:
# Input: root = [0,1,0,0,1,0,None,None,1,0,0], arr = [0,0,1]
# Output: false
# Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.

# Example 3:
# Input: root = [0,1,0,0,1,0,None,None,1,0,0], arr = [0,1,1]
# Output: false
# Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.

# Constraints:
# 1 <= arr.length <= 5000
# 0 <= arr[i] <= 9
# Each node's value is between [0 - 9].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List


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

    def isValidBranch(self, node, arr, i, len) -> bool:
        if not node or node.val != arr[i]: return False
        if i == len - 1:
            return node.left is None and node.right is None
        return self.isValidBranch(node.left, arr, i + 1, len) or self.isValidBranch(node.right, arr, i + 1, len)


    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return  self.isValidBranch(root, arr, 0, len(arr))
        # p = None
        # for v in arr:
        #     print("-------------------")
        #     print("v = ", v)
        #     if p:
        #         print("p.left = ", p.left)
        #         print("p.right = ", p.right)
        #         if p.left: print(">>> left = ", p.left.val)
        #         if p.right: print(">>> right = ", p.right.val)

        #         if p.left and p.left.val == v:
        #             p = p.left
        #         elif p.right and p.right.val == v:
        #             p = p.right
        #         else: return False
        #     else:
        #         p = root
        #         print(".... root p.val = ", p.val)
        #         if p.val != v: return False
        # return p.left is None and p.right is None

t = Solution()

print("True = ", t.isValidSequence(t.fromArray([0,1,0,0,1,0,None,None,1,0,0], 0), [0,1,0,1]))
print("False = ", t.isValidSequence(t.fromArray([0,1,0,0,1,0,None,None,1,0,0], 0), [0,0,1]))
print("False = ", t.isValidSequence(t.fromArray([0,1,0,0,1,0,None,None,1,0,0], 0), [0,1,1]))

tree = [0,9,0,5,6,6,9,2,8,1,6,9,5,6,3,1,4,1,9,9,1,0,1,9,7,0,4,6,5,2,7,3,3,6,9,8,2,9,1,8,5,9,2,None,5,3,4,7,6,5,3,2,7,6,4,0,2,0,5,8,4,1,2,9,0,None,2,7,8,7,4,9,None,9,3,9,7,0,7,3,7,None,7,3,5,4,1,1,8,None,7,7,9,4,2,6,0,None,5,5,4,1,0,7,4,9,8,2,8,5,2,None,None,1,9,0,5,7,3,None,None,9,4,3,6,2,9,1,1,8,5,0,None,8,None,6,8,4,5,2,3,None,None,None,None,0,None,2,9,1,None,None,None,8,None,7,None,1,1,None,5,8,9,5,6,None,4,5,9,None,4,6,None,None,1,8,None,6,3,4,5,7,3,3,9,8,None,0,1,3,9,9,0,4,3,1,3,9,2,1,9,5,None,1,8,3,6,None,None,5,3,None,2,2,4,6,9,8,2,None,5,2,None,None,4,1,6,None,9,5,8,3,None,None,8,3,None,7,6,None,6,4,None,None,None,None,None,7,0,9,4,6,5,2,3,None,0,2,1,None,None,8,3,None,None,None,None,None,None,1,0,None,None,None,4,None,9,None,7,None,None,5,7,None,2,None,0,None,5,None,None,None,None,None,0,4,None,2,3,2,None,5,None,1,5,3,None,None,6,2,4,1,9,9,3,None,None,3,9,0,None,7,7,2,8,9,8,8,2,6,9,4,6,3,0,5,0,8,None,None,5,5,6,3,0,6,9,0,0,1,0,1,0,7,2,None,None,None,None,None,None,None,None,0,6,8,4,None,5,3,0,9,None,None,None,None,5,7,9,0,8,4,6,3,5,9,None,None,None,None,None,None,None,None,None,9,9,0,None,None,9,1,9,6,6,None,1,2,None,2,4,4,7,5,4,0,1,4,9,None,8,3,None,None,None,0,None,4,None,None,6,None,None,None,None,None,None,None,None,4,None,None,None,None,None,None,None,None,None,0,None,None,None,None,None,None,None,2,8,None,None,8,6,1,6,None,4,1,2,0,None,None,0,2,None,2,7,7,0,6,4,1,4,1,9,9,7,0,8,7,7,3,5,7,1,8,None,2,8,9,None,5,4,0,5,4,None,3,6,5,7,0,4,None,5,7,8,8,2,None,None,None,None,3,4,None,1,8,6,4,7,7,7,6,None,8,8,None,1,0,9,None,None,5,8,4,7,None,7,None,3,2,None,None,None,None,4,0,3,3,5,8,2,None,7,4,9,None,None,None,0,4,8,3,0,7,0,4,None,3,None,None,None,6,8,6,None,1,2,2,6,None,None,None,None,3,7,None,0,7,1,5,3,None,None,9,6,None,None,None,7,7,2,6,3,None,None,9,7,0,9,0,None,4,5,1,3,2,None,None,None,7,None,None,None,None,None,None,None,None,9,None,None,5,9,None,9,None,None,9,6,None,2,None,None,None,None,None,None,6,None,7,9,2,6,4,3,None,0,None,None,1,3,1,4,3,4,7,None,None,None,None,None,0,None,7,6,3,4,None,3,3,9,None,None,8,8,6,4,0,None,4,0,None,4,None,6,3,6,7,None,None,None,0,2,6,0,8,2,None,9,4,1,5,9,9,1,0,0,4,6,1,1,3,None,6,0,3,7,1,3,7,4,9,0,None,4,9,None,None,9,4,0,2,6,4,None,None,None,0,None,3,3,4,6,None,None,4,None,None,None,5,None,None,3,0,3,None,None,9,1,0,None,6,8,2,None,None,None,None,5,None,None,5,None,8,None,None,None,6,None,4,None,5,None,0,None,None,7,3,None,None,None,9,None,None,1,9,4,None,4,2,None,None,None,3,7,None,None,None,5,7,None,None,None,8,None,None,None,None,None,None,None,5,None,None,None,None,2,3,6,None,None,1,None,3,3,None,None,None,None,None,2,4,0,None,7,None,2,4,1,2,6,None,0,None,8,None,8,8,0,None,8,0,None,0,None,None,9,None,None,None,None,4,2,4,8,None,None,None,None,None,7,None,None,None,None,None,5,1,None,None,None,8,None,9,4,None,None,1,None,7,5,8,9,0,None,None,None,None,None,1,2,7,None,None,1,2,7,4,8,6,6,4,0,9,3,None,None,2,None,None,None,None,None,None,None,None,None,8,None,0,None,5,3,4,None,4,7,5,None,None,None,None,9,6,0,7,4,7,4,7,0,None,0,9,1,3,None,9,None,None,None,6,1,None,None,2,9,9,5,2,9,None,None,5,8,5,4,8,1,9,6,9,9,7,8,5,None,0,4,9,2,1,7,3,8,7,9,None,0,3,9,7,9,8,None,3,5,None,None,0,6,None,None,2,6,None,9,None,None,0,None,None,None,None,None,None,None,2,None,None,None,None,1,None,4,None,None,2,6,0,2,0,2,None,None,None,None,None,0,2,9,5,4,None,None,None,None,1,8,None,4,None,None,None,7,None,4,None,None,None,5,None,9,None,None,6,None,9,6,None,3,None,None,None,None,3,None,None,None,9,1,None,None,7,None,None,6,8,None,None,None,None,None,None,None,4,None,None,None,9,None,None,None,None,None,9,8,None,0,7,1,2,0,None,None,None,None,None,None,7,None,None,None,None,None,None,None,None,None,None,None,2,1,None,None,5,None,None,None,5,None,None,6,None,None,None,None,None,1,None,None,9,None,3,6,None,None,1,9,3,1,2,7,8,None,None,None,1,None,None,None,None,None,8,9,0,None,9,None,1,None,None,None,5,1,7,None,3,0,None,None,None,0,None,None,None,None,3,4,None,None,2,None,0,None,6,None,None,None,None,None,9,None,2,3,4,4,0,9,7,4,6,None,None,None,5,0,None,6,None,None,None,5,2,7,None,5,None,8,None,6,0,4,None,None,6,1,0,6,6,None,2,None,None,7,5,2,7,None,0,2,7,None,3,3,3,None,6,3,2,4,None,1,9,None,2,None,1,8,None,7,4,0,0,2,3,3,None,None,None,None,None,None,5,2,7,4,4,7,7,None,8,7,None,None,None,None,None,None,7,8,None,None,None,None,None,7,1,0,None,1,None,8,None,None,None,None,None,None,None,2,1,5,None,None,None,None,2,6,None,None,8,5,4,4,0,1,None,7,8,None,None,None,None,0,None,4,5,0,2,None,3,9,None,None,None,4,9,None,9,None,None,None,7,7,None,0,None,None,None,5,None,6,0,0,None,None,None,None,None,None,None,None,None,9,None,None,0,None,3,7,None,6,None,None,None,None,None,None,None,1,9,6,None,7,1,2,7,3,7,4,None,None,None,None,None,None,3,1,1,9,2,6,None,None,None,3,9,0,3,1,None,None,None,None,4,None,None,0,None,None,None,1,9,0,None,0,2,8,6,None,None,None,None,None,1,None,6,4,None,None,None,None,None,None,None,None,6,None,None,1,None,None,None,None,6,4,6,7,None,None,4,5,None,None,None,4,None,4,None,3,None,1,8,5,None,4,None,None,None,6,4,1,1,0,0,0,6,4,None,3,4,6,9,None,2,None,None,4,None,None,8,None,None,None,None,None,None,None,None,None,0,8,None,6,None,None,2,0,8,None,9,7,None,None,3,7,None,None,8,None,None,0,2,None,1,None,6,4,5,0,0,9,7,4,None,9,5,7,3,4,None,None,None,4,7,3,None,5,4,None,9,None,None,6,7,None,None,None,None,None,None,None,5,2,None,None,None,None,7,None,None,None,3,8,7,None,None,None,None,None,0,3,None,None,7,5,None,None,2,8,None,None,None,0,None,None,None,None,None,None,None,None,None,4,None,None,6,3,None,None,None,None,None,None,None,None,9,0,8,None,6,1,None,None,None,9,None,None,None,4,3,None,None,None,5,None,8,3,2,9,5,7,None,3,6,None,1,None,3,3,None,None,8,None,None,None,None,None,None,None,2,1,3,6,None,None,7,None,2,None,None,None,None,None,None,4,9,None,3,None,5,None,None,5,None,None,None,None,None,None,None,None,None,4,None,None,1,None,2,None,None,None,None,None,None,None,None,None,None,2,0,0,None,None,None,None,4,3,4,1,8,7,6,1,3,None,None,8,None,None,None,None,None,None,None,None,None,7,None,None,5,9,None,None,None,0,9,5,4,1,9,None,0,3,8,5,None,9,6,0,None,2,9,8,1,None,None,None,2,None,0,2,None,8,None,None,None,6,7,0,0,6,4,None,2,0,None,None,None,9,None,2,5,3,None,None,None,None,None,9,5,None,6,1,None,0,3,6,8,1,6,1,None,6,9,2,0,8,8,5,1,8,2,8,0,None,None,None,None,7,None,None,None,None,None,None,None,None,None,4,None,4,None,8,7,None,None,None,None,None,8,6,None,5,2,None,None,None,None,None,8,None,None,6,None,8,None,None,None,None,None,None,5,None,None,None,9,7,0,0,None,None,None,None,None,8,None,1,None,None,None,None,None,None,None,None,2,None,7,7,None,7,4,None,None,None,None,None,None,None,8,None,None,None,1,None,0,2,None,None,None,None,None,3,None,3,6,9,5,None,0,None,1,None,None,6,None,4,None,None,None,None,None,5,None,None,6,None,7,0,6,8,3,None,5,None,7,7,None,None,2,None,5,None,None,9,None,6,None,None,None,1,None,None,None,None,None,None,None,None,None,None,5,None,None,None,None,2,6,6,None,9,None,4,None,2,9,3,None,None,3,7,2,1,5,6,None,None,None,None,0,None,6,7,2,0,5,None,None,None,None,6,None,6,7,None,None,None,4,None,None,4,None,5,None,None,None,None,None,None,None,None,8,5,None,None,None,0,7,8,None,0,1,6,9,7,5,0,None,9,7,1,None,None,None,None,None,None,None,None,8,2,None,6,None,3,1,3,1,4,6,3,5,5,4,5,None,None,None,None,7,3,None,None,None,3,None,6,None,None,5,None,4,9,4,None,3,None,None,None,None,None,None,None,None,None,None,None,9,None,None,None,None,None,None,6,None,None,None,None,3,6,None,None,None,None,None,None,3,None,None,None,None,None,4,None,None,None,None,None,None,6,None,None,1,None,None,None,None,None,None,None,None,None,None,None,None,8,None,9,5,None,9,6,0,7,3,9,None,None,3,9,None,None,4,None,None,None,None,None,None,None,None,1,8,None,None,None,None,7,None,6,7,5,None,None,6,5,None,None,None,None,None,None,None,None,None,0,1,None,None,None,8,0,0,3,None,None,None,None,None,0,0,None,None,None,6,3,None,4,5,3,None,None,None,9,None,None,None,None,None,7,5,4,8,6,5,1,None,4,5,3,None,8,1,2,7,6,8,9,6,None,None,None,None,None,6,None,3,7,None,None,6,0,None,None,None,None,6,4,9,2,9,3,1,None,5,7,None,None,None,None,1,1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,0,None,None,None,2,None,None,6,None,None,None,None,None,None,7,None,None,None,None,0,8,None,None,3,None,None,None,None,None,None,None,None,None,3,None,None,None,None,None,None,None,None,5,None,None,None,None,9,None,5,None,4,None,None,None,None,None,None,None,2,None,None,None,7,None,None,1,5,7,8,None,None,8,None,None,1,None,3,None,None,4,6,None,None,9,None,None,None,1,2,4,None,1,1,None,None,3,None,4,3,None,None,None,5,6,0,6,4,3,8,None,9,None,None,None,9,None,None,None,0,7,None,None,3,None,9,8,1,2,7,7,None,None,4,None,6,8,3,9,None,None,2,None,None,8,None,None,None,8,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,5,None,None,7,None,None,None,None,None,None,None,None,None,5,None,None,None,None,0,None,None,None,None,None,None,None,None,None,None,None,4,None,3,None,8,2,0,None,None,None,None,0,None,None,6,None,None,None,7,None,None,8,3,0,None,None,None,None,None,None,4,4,None,None,None,None,1,None,None,3,None,None,2,None,5,8,None,None,None,None,None,None,None,None,None,7,None,None,None,None,None,None,None,None,None,None,None,None,None,2,None,None,None,None,None,None,None,None,None,None,3,8,3,5,None,None,None,4,None,None,8,None,0,0,None,2,None,1,None,7,None,5,9,2,None,None,None,9,3,0,3,None,None,None,None,6,0,6,None,5,8,None,7,7,None,None,None,None,None,2,4,9,None,None,None,None,None,5,None,6,None,None,None,None,None,None,5,None,None,None,None,None,None,8,None,9]
arr = [0,0,6,9,9,7,4,6,2,8,9,4,5,7,3,8]

print("True = ", t.isValidSequence(t.fromArray(tree, 0), arr))