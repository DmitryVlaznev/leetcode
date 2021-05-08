# 109. Convert Sorted List to Binary Search Tree

# Medium

# Given the head of a singly linked list where elements are sorted in
# ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary
# tree in which the depth of the two subtrees of every node never differ
# by more than 1.

# Example 1:
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which
# represents the shown height balanced BST.

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [0]
# Output: [0]

# Example 4:
# Input: head = [1,3]
# Output: [3,1]

# Constraints:
# The number of nodes in head is in the range [0, 2 * 104].
# -10^5 <= Node.val <= 10^5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List
from utils import TreeNode, ListNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def createNode(left: ListNode, left_idx: int, right: ListNode, right_idx: int):
            if right_idx == left_idx:
                return TreeNode(left.val)
            import math

            mid = math.ceil((right_idx - left_idx) / 2)
            p, c = left, mid
            while c > 1:
                p = p.next
                c -= 1
            node = TreeNode(p.next.val)
            node.left = createNode(left, left_idx, p, left_idx + mid - 1)
            right_left = left_idx + mid + 1
            if right_left <= right_idx:
                node.right = createNode(p.next.next, right_left, right, right_idx)
            return node

        if not head:
            return None
        p, c = head, 0
        while p.next:
            c += 1
            p = p.next

        return createNode(head, 0, p, c)
