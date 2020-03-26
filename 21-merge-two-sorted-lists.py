# 21. Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a new list. The new
# list should be made by splicing together the nodes of the first two
# lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

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

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        head = tail = p = None
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val <= p2.val:
                p = p1
                p1 = p1.next
            else:
                p = p2
                p2 = p2.next

            if head:
                tail.next = p
                tail = tail.next
            else:
                head = tail = p

        if p1:
            p.next = p1
        elif p2:
            p.next = p2

        return head



test = Solution()
print(">> ", test.toArray(test.mergeTwoLists(test.fromArray([1, 2, 3]), test.fromArray([11, 12, 13]))))
print(">> ", test.toArray(test.mergeTwoLists(test.fromArray([1, 2, 3]), test.fromArray([11, 12, 13, 14, 15]))))
print(">> ", test.toArray(test.mergeTwoLists(test.fromArray([1, 2, 3, 4, 5]), test.fromArray([11, 12, 13]))))
print(">> ", test.toArray(test.mergeTwoLists(test.fromArray([1, 2]), test.fromArray([]))))
print(">> ", test.toArray(test.mergeTwoLists(test.fromArray([]), test.fromArray([1, 2]))))
print(">> ", test.toArray(test.mergeTwoLists(test.fromArray([]), test.fromArray([]))))
print(">> ", test.toArray(test.mergeTwoLists(test.fromArray([1]), test.fromArray([11, 12]))))
print(">> ", test.toArray(test.mergeTwoLists(test.fromArray([1, 2]), test.fromArray([11]))))
print(">> ", test.toArray(test.mergeTwoLists(test.fromArray([1, 2, 2]), test.fromArray([1, 1, 1, 2]))))
print(">> ", test.toArray(test.mergeTwoLists(test.fromArray([2]), test.fromArray([1]))))