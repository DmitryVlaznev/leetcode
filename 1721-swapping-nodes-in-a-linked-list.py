# 1721. Swapping Nodes in a Linked List

# Medium

# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the
# kth node from the beginning and the kth node from the end (the list is
# 1-indexed).

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]

# Example 3:
# Input: head = [1], k = 1
# Output: [1]

# Example 4:
# Input: head = [1,2], k = 1
# Output: [2,1]

# Example 5:
# Input: head = [1,2,3], k = 2
# Output: [1,2,3]

# Constraints:
# The number of nodes in the list is n.
# 1 <= k <= n <= 10^5
# 0 <= Node.val <= 100

from utils import ListNode, listFromArray, listToArray, checkList


class Solution:
    def swapNodes2(self, head: ListNode, k: int) -> ListNode:
        l, p = 1, head
        pp = a = pre_a = b = pre_b = None
        while p:
            if l == k:
                a, pre_a = p, pp
                b = head

            if l > k:
                pre_b = b
                b = b.next
            l += 1
            pp = p
            p = p.next

        if a == b:
            return head

        new_head = head
        if head == a:
            new_head = b
        elif head == b:
            new_head = a

        if pre_b == a:
            a.next = b.next
            b.next = a
            if pre_a:
                pre_a.next = b
            return new_head

        if pre_a == b:
            b.next = a.next
            a.next = b
            if pre_b:
                pre_b.next = a
            return new_head

        t = a.next
        a.next = b.next
        b.next = t
        if pre_a:
            pre_a.next = b
        if pre_b:
            pre_b.next = a
        return new_head

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        l, p = 1, head
        a = b = None
        while p:
            if l == k:
                a = p
                b = head

            if l > k:
                b = b.next
            l += 1
            p = p.next

        a.val, b.val = b.val, a.val
        return head


t = Solution()

checkList(
    [1, 6, 3, 4, 5, 2, 7],
    listToArray(t.swapNodes(listFromArray([1, 2, 3, 4, 5, 6, 7]), 2)),
)
checkList(
    [7, 2, 3, 4, 5, 6, 1],
    listToArray(t.swapNodes(listFromArray([1, 2, 3, 4, 5, 6, 7]), 1)),
)
checkList(
    [1, 2, 3, 4, 5, 6, 7],
    listToArray(t.swapNodes(listFromArray([1, 2, 3, 4, 5, 6, 7]), 4)),
)
checkList(
    [1, 2, 5, 4, 3, 6, 7],
    listToArray(t.swapNodes(listFromArray([1, 2, 3, 4, 5, 6, 7]), 5)),
)
checkList(
    [7, 2, 3, 4, 5, 6, 1],
    listToArray(t.swapNodes(listFromArray([1, 2, 3, 4, 5, 6, 7]), 7)),
)

checkList([1], listToArray(t.swapNodes(listFromArray([1]), 1)))
checkList([2, 1], listToArray(t.swapNodes(listFromArray([1, 2]), 1)))
checkList([1, 3, 2, 4], listToArray(t.swapNodes(listFromArray([1, 2, 3, 4]), 2)))
checkList([1, 3, 2, 4], listToArray(t.swapNodes(listFromArray([1, 2, 3, 4]), 3)))
checkList([2, 1], listToArray(t.swapNodes(listFromArray([1, 2]), 2)))
