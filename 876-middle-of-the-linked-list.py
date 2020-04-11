# 876. Middle of the Linked List

# Middle of the Linked List

# Given a non-empty, singly linked list with head node head, return a
# middle node of linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])

# The returned node has value 3.  (The judge's serialization of this
# node is [3,4,5]).

# Note that we returned a ListNode object ans, such that: ans.val = 3,
# ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next =
# NULL.

# Example 2:
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second one.


# Note:
# The number of nodes in the given list will be between 1 and 100.

# Definition for singly-linked list.

from typing import List


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

    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if fast: fast = fast.next
        return slow

t = Solution()
print("[3, 4, 5]", t.toArray(t.middleNode(t.fromArray([1,2,3,4,5]))))
print("[4, 5, 6]", t.toArray(t.middleNode(t.fromArray([1,2,3,4,5,6]))))
print("[1]", t.toArray(t.middleNode(t.fromArray([1]))))
print("[2]", t.toArray(t.middleNode(t.fromArray([1,2]))))
print("[2, 3]", t.toArray(t.middleNode(t.fromArray([1,2,3]))))