# 61. Rotate List

# Given a linked list, rotate the list to the right by k places, where k
# is non-negative.

# Example 1:
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL

# Example 2:
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL

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

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Find the length of the list, 1 pass
        current_tail = head
        l = 1
        while current_tail and current_tail.next:
            current_tail = current_tail.next
            l += 1

        if l < 2:
            return head

        if k % l == 0:
            return head

        # Find the new tail of the list, 1 pass
        tail_index = l - k % l
        tail = head
        i = 1
        while i < tail_index:
            i += 1
            tail = tail.next

        current_tail.next = head
        head = tail.next
        tail.next = None
        return head

test = Solution()
print("[4, 5, 1, 2, 3] >> ", test.toArray(test.rotateRight(test.fromArray([1, 2, 3, 4, 5]), 2)))
print("[4, 5, 1, 2, 3] >> ", test.toArray(test.rotateRight(test.fromArray([1, 2, 3, 4, 5]), 7)))
print("[5, 1, 2, 3, 4] >> ", test.toArray(test.rotateRight(test.fromArray([1, 2, 3, 4, 5]), 1)))
print("[1, 2, 3, 4, 5] >> ", test.toArray(test.rotateRight(test.fromArray([1, 2, 3, 4, 5]), 10)))
print("[1] >> ", test.toArray(test.rotateRight(test.fromArray([1]), 3)))
print("[1, 2] >> ", test.toArray(test.rotateRight(test.fromArray([1, 2]), 42)))
print("[2, 1] >> ", test.toArray(test.rotateRight(test.fromArray([1, 2]), 43)))
print("[] >> ", test.toArray(test.rotateRight(test.fromArray([]), 43)))