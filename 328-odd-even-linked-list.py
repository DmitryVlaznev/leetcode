# 328. Odd Even Linked List

# Given a singly linked list, group all odd nodes together followed by
# the even nodes. Please note here we are talking about the node number
# and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.

# Example 1:
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL

# Example 2:
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL

# Note:
# * The relative order inside both the even and odd groups should remain
#   as it was in the input.
# * The first node is considered odd, the second node even and so on ...

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

    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        head_odd = head
        head_even = head_odd.next
        if not head_even or not head_even.next:
            return head

        p_odd = head_odd
        tail_odd = p_odd
        p_even = head_even
        while p_odd:
            next_odd = p_even.next if p_even else None
            next_even = next_odd.next if next_odd else None

            p_odd.next = next_odd
            if next_odd:
                tail_odd = next_odd
            p_odd = next_odd

            if p_even:
                p_even.next = next_even
                p_even = next_even

        tail_odd.next = head_even
        return head_odd

test = Solution()

print("[1, 3, 5, 2, 4] >> ", test.toArray(test.oddEvenList(test.fromArray([1, 2, 3, 4, 5]))))
print("[1, 3, 2, 4] >> ", test.toArray(test.oddEvenList(test.fromArray([1, 2, 3, 4]))))
print("[1, 2] >> ", test.toArray(test.oddEvenList(test.fromArray([1, 2]))))
print("[1] >> ", test.toArray(test.oddEvenList(test.fromArray([1]))))
print("[] >> ", test.toArray(test.oddEvenList(test.fromArray([]))))
