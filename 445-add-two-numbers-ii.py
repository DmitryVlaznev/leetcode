# 445. Add Two Numbers II

# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their
# nodes contain a single digit. Add the two numbers and return it as a
# linked list.

# You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing
# the lists is not allowed.

# Example:
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

from utils import ListNode, listFromArray, listToArray, checkList


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return None

        def get_len(p):
            l = 0
            while p:
                l += 1
                p = p.next
            return l

        def reverse(head):
            prv, cur, nxt = None, head, head.next
            while cur:
                cur.next = prv
                prv = cur
                cur = nxt
                nxt = nxt.next if nxt else None
            return prv

        l1_len = get_len(l1)
        l2_len = get_len(l2)
        short = l1 if l1_len < l2_len else l2
        long = l2 if short == l1 else l1
        sum_start = max(l1_len, l2_len) - min(l1_len, l2_len)

        p = head = ListNode(None)
        for i in range(max(l1_len, l2_len)):
            if i < sum_start:
                p.next = ListNode(long.val)
            else:
                p.next = ListNode(long.val + short.val)
                short = short.next
            long = long.next
            p = p.next

        head = reverse(head)
        p = head
        carry = 0
        while p.next.val is not None:
            p.val += carry
            if p.val > 9:
                carry = 1
                p.val = p.val % 10
            else:
                carry = 0
            p = p.next

        p.val += carry
        if p.val > 9:
            p.val = p.val % 10
            p.next.val = 1
        else:
            p.next = None

        return reverse(head)


t = Solution()

checkList(
    [1, 0, 3, 3, 0, 7, 5, 0, 8, 9],
    listToArray(
        t.addTwoNumbers(
            listFromArray([6, 4, 5, 0, 4, 4, 9, 4, 1]),
            listFromArray([3, 8, 8, 0, 3, 0, 1, 4, 8]),
        )
    ),
)

checkList(
    [7, 8, 0, 7],
    listToArray(t.addTwoNumbers(listFromArray([7, 2, 4, 3]), listFromArray([5, 6, 4]))),
)

checkList(
    [1, 0, 4, 6, 0],
    listToArray(t.addTwoNumbers(listFromArray([5, 6, 4]), listFromArray([9, 8, 9, 6]))),
)

checkList(
    [5],
    listToArray(t.addTwoNumbers(listFromArray([2]), listFromArray([3]))),
)

checkList(
    [1, 5],
    listToArray(t.addTwoNumbers(listFromArray([6]), listFromArray([9]))),
)

checkList(
    [5, 6, 7],
    listToArray(t.addTwoNumbers(listFromArray([2, 3, 4]), listFromArray([3, 3, 3]))),
)

checkList(
    [1, 7, 7, 7],
    listToArray(t.addTwoNumbers(listFromArray([8, 8, 8]), listFromArray([8, 8, 9]))),
)

checkList(
    [0],
    listToArray(t.addTwoNumbers(listFromArray([0]), listFromArray([0]))),
)