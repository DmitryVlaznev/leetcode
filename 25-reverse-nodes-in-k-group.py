# 25. Reverse Nodes in k-Group

# Given a linked list, reverse the nodes of a linked list k at a time
# and return its modified list.

# k is a positive integer and is less than or equal to the length of the
# linked list. If the number of nodes is not a multiple of k then
# left-out nodes in the end should remain as it is.

# Example:
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5

# Note:
# * Only constant extra memory is allowed.
# * You may not alter the values in the list's nodes, only nodes itself
#   may be changed.

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or not head:
            return head

        tail = prev = None
        p = group_tail = head
        gc = 0
        while p:
            if gc == k:
                if tail:
                    tail.next = prev
                else:
                    head = prev
                tail = group_tail
                group_tail.next = p
                group_tail = p
                prev = None
                gc = 0
            else:
                next = p.next
                p.next = prev
                prev = p
                p = next
                gc += 1

        if gc == k:
            if tail:
                tail.next = prev
            else:
                head = prev
        else:
            p = prev
            prev = None
            while p:
                next = p.next
                p.next = prev
                prev = p
                p = next
        return head

test = Solution()

print("[3, 2, 1, 6, 5, 4, 9, 8, 7] >> ", test.toArray(test.reverseKGroup(test.fromArray([1, 2, 3, 4, 5, 6, 7, 8, 9]), 3)))
print("[3, 2, 1, 6, 5, 4, 7, 8] >> ", test.toArray(test.reverseKGroup(test.fromArray([1, 2, 3, 4, 5, 6, 7, 8]), 3)))
print("[1, 2, 3] >> ", test.toArray(test.reverseKGroup(test.fromArray([1, 2, 3]), 4)))