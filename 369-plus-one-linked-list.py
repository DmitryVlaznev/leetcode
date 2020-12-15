# 369. Plus One Linked List

# Medium

# Given a non-negative integer represented as a linked list of digits,
# plus one to the integer.

# The digits are stored such that the most significant digit is at the
# head of the list.

# Example 1:
# Input: head = [1,2,3]
# Output: [1,2,4]

# Example 2:
# Input: head = [0]
# Output: [1]

# Constraints:
# * The number of nodes in the linked list is in the range [1, 100].
# * 0 <= Node.val <= 9
# * The number represented by the linked list does not contain leading
#   zeros except for the zero itself.

from utils import ListNode, listFromArray, listToArray, checkList


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        if not head:
            return None
        h, p = head, head.next
        head.next = None
        while p:
            t, p.next, h = p.next, h, p
            p = t
        return h

    def plusOne(self, head: ListNode) -> ListNode:
        if not head:
            return None
        h = p = self.reverse(head)
        acc = 1
        while acc:
            p.val += acc
            if p.val == 10:
                p.val = 0
                if not p.next:
                    p.next = ListNode(0)
            else:
                acc = 0
            p = p.next
        return self.reverse(h)


t = Solution()
checkList([1, 2, 4], listToArray(t.plusOne(listFromArray([1, 2, 3]))))
checkList([9, 0], listToArray(t.plusOne(listFromArray([8, 9]))))
checkList([1, 0, 0], listToArray(t.plusOne(listFromArray([9, 9]))))
checkList([1], listToArray(t.plusOne(listFromArray([0]))))
