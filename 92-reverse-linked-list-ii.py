# 92. Reverse Linked List II

# Reverse a linked list from position m to n. Do it in one-pass.

# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:

# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

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

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        c = n - m
        if not c:
            return head

        subtail = None
        while m > 1:
            subtail = subtail.next if subtail else head
            m -= 1

        prev = None
        subhead = subtail.next if subtail else head
        cur = subhead
        while c >= 0:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            c -= 1
        subhead.next = cur
        if subtail:
            subtail.next = prev
        else:
            head = prev

        return head


test = Solution()

print("[1, 4, 3, 2, 5] >> ", test.toArray(test.reverseBetween(test.fromArray([1, 2, 3, 4, 5]), 2, 4)))
print("[3, 2, 1, 4, 5] >> ", test.toArray(test.reverseBetween(test.fromArray([1, 2, 3, 4, 5]), 1, 3)))
print("[1, 2, 3, 5, 4] >> ", test.toArray(test.reverseBetween(test.fromArray([1, 2, 3, 4, 5]), 4, 5)))
print("[5, 4, 3, 2, 1] >> ", test.toArray(test.reverseBetween(test.fromArray([1, 2, 3, 4, 5]), 1, 5)))
print("[1, 2, 3, 4, 5] >> ", test.toArray(test.reverseBetween(test.fromArray([1, 2, 3, 4, 5]), 3, 3)))
print("[2, 1] >> ", test.toArray(test.reverseBetween(test.fromArray([1, 2]), 1, 2)))
print("[2] >> ", test.toArray(test.reverseBetween(test.fromArray([2]), 1, 1)))
