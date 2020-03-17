# 206. Reverse Linked List

# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could
# you implement both?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List


class Solution:
    @staticmethod
    def fromArray(values: List) -> ListNode:
        l = len(values)
        if not l:
            return None
        head = ListNode(values[0])
        cur = head
        for i in range(1, l):
            cur.next = ListNode(values[i])
            cur = cur.next
        return head

    @staticmethod
    def toArray(head: ListNode) -> List:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        return self._reverseRecursive(None, head);

    def _reverseRecursive(self, parent: ListNode, node: ListNode) -> ListNode:
        if not node:
            return parent
        head = self._reverseRecursive(node, node.next)
        node.next = parent
        return head

test = Solution()

# test from-to array
print("[] >> ", test.toArray(test.fromArray([])))
print("[1, 2, 3] >> ", test.toArray(test.fromArray([1, 2, 3])))

# test iterative algorithm
print("[3, 2, 1] >> ", test.toArray(test.reverseList(test.fromArray([1, 2, 3]))))

# test recursive algorithm
print("[3, 2, 1] >> ", test.toArray(test.reverseListRecursive(test.fromArray([1, 2, 3]))))