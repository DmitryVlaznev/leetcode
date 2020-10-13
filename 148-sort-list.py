# 148. Sort List

# Given the head of a linked list, return the list after sorting it in
# ascending order.

# Follow up: Can you sort the linked list in O(n log n) time and O(1)
# memory (i.e. constant space)?


# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Example 3:
# Input: head = []
# Output: []


# Constraints:
# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from utils import ListNode, listFromArray, listToArray, checkList

class Solution:
    def merge(self, h1, h2, right):
        p = h1
        while p:
            if p.next == h2: p.next, p = None, h2
            elif p.next == right: p.next = p = None
            else: p = p.next

        head, tail, p1, p2 = None, None, h1, h2
        while p1 or p2:
            t = None
            if p1 and p2:
                if p1.val < p2.val: t, p1 = p1, p1.next
                else: t, p2 = p2, p2.next
            elif p1: t, p1 = p1, p1.next
            else:  t, p2 = p2, p2.next
            t.next = None

            if not head: head = tail = t
            else: tail.next, tail = t, t
        return head, tail

    def sortList(self, head: ListNode) -> ListNode:
        nodes, p = 0, head
        while p: nodes, p = nodes + 1, p.next
        if nodes < 2: return head

        subarray_length = 1
        while subarray_length < nodes:
            p, left = head, None
            while p:
                q, d = p, subarray_length
                while q and d: q, d = q.next, d - 1
                if q:
                    right, d = q, subarray_length
                    while right and d: right, d = right.next, d - 1
                    sub_head, sub_tail = self.merge(p, q, right)
                    sub_tail.next = right

                    if left: left.next = sub_head
                    else: head = sub_head

                    left, p = sub_tail, right
                else:
                    p = p.next

            subarray_length *= 2
        return head

t = Solution()
checkList([1,2,3,4], listToArray(t.sortList(listFromArray([4,2,1,3]))))
checkList([1,2,3], listToArray(t.sortList(listFromArray([3,2,1]))))
checkList([1,2,3,4,5,6,7], listToArray(t.sortList(listFromArray([7,1,4,2,3,6,5]))))
checkList([-1,0,3,4,5], listToArray(t.sortList(listFromArray([-1,5,3,4,0]))))
checkList([5], listToArray(t.sortList(listFromArray([5]))))
checkList([], listToArray(t.sortList(listFromArray([]))))
