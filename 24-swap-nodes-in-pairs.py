# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its
# head.

# You may not modify the values in the list's nodes, only nodes itself
# may be changed.

 # Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.

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

    def swapPairs(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur and cur.next:
            next = cur.next.next
            if prev:
                prev.next = cur.next
            else:
                head = cur.next
            prev = cur

            cur.next.next = cur
            cur.next = next
            cur = next

        return head

test = Solution()
print("[2, 1, 4, 3] >> ", test.toArray(test.swapPairs(test.fromArray([1, 2, 3, 4]))))
print("[2, 1, 4, 3, 5] >> ", test.toArray(test.swapPairs(test.fromArray([1, 2, 3, 4, 5]))))
print("[] >> ", test.toArray(test.swapPairs(test.fromArray([]))))
print("[1] >> ", test.toArray(test.swapPairs(test.fromArray([1]))))
print("[2, 1] >> ", test.toArray(test.swapPairs(test.fromArray([1, 2]))))
print("[2, 1, 3] >> ", test.toArray(test.swapPairs(test.fromArray([1, 2, 3]))))