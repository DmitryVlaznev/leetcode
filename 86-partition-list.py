# 86. Partition List

# Medium

# Given the head of a linked list and a value x, partition it such that
# all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each
# of the two partitions.

# Example 1:
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:
# Input: head = [2,1], x = 2
# Output: [1,2]

# Constraints:

# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

from utils import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lh = lp = ListNode(-1)
        gh = gp = ListNode(-1)
        p = head
        while p:
            t = p.next
            if p.val < x:
                lp.next = p
                lp = p
            else:
                gp.next = p
                gp = p
            p.next = None
            p = t
        head = lh.next
        if head:
            lp.next = gh.next
        else:
            head = gh.next
        lh.next = gh.next = None
        return head