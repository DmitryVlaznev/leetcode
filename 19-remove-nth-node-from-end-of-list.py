# 19. Remove Nth Node From End of List

# Medium

# Given the head of a linked list, remove the nth node from the end of
# the list and return its head.

# Follow up: Could you do this in one pass?

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

from utils import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p, q = head, None
        while p:
            if n == 0:
                q = head
            elif n < 0:
                q = q.next
            p = p.next
            n -= 1
        if q:
            t = q.next
            q.next = q.next.next
        else:
            t = head
            head = head.next
        t.next = None
        return head