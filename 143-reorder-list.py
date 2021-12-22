# 143. Reorder List

# Medium

# You are given the head of a singly linked-list. The list can be
# represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes
# themselves may be changed.


# Example 1:

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]


# Constraints:
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000

from typing import Optional
from utils import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p, l = head, 1
        while p.next:
            p, l = p.next, l + 1
        if l <= 2:
            return

        tail_start = l // 2 + l % 2
        tail, l, last = head, 0, None
        while l < tail_start:
            last = tail
            tail, l = tail.next, l + 1
        last.next = None

        p, q = tail, None
        while p:
            t = p.next
            p.next = q
            q = p
            p = t
        tail = q

        p, q = head, tail
        while p and q:
            pt, qt = p.next, q.next
            p.next, q.next = q, pt
            p, q = pt, qt