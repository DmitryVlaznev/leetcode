# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their
# nodes contain a single digit. Add the two numbers and return it as a
# linked list.

# You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

from typing import List
import utils

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        acc = 0
        res = tail = None

        while p or q:
            digit = 0
            digit += acc
            if p:
                digit += p.val
                p = p.next
            if q:
                digit += q.val
                q = q.next

            acc = digit // 10
            digit = digit % 10
            node = ListNode(digit)
            if res:
                tail.next = node
                tail = node
            else: res = tail = node

        if acc: tail.next = ListNode(acc)
        return res

t = Solution()
# 342 + 465 = 807
utils.checkList([7, 0, 8], utils.listToArray(t.addTwoNumbers(utils.listFromArray([2, 4, 3]), utils.listFromArray([5, 6, 4]))))
# 342 + 465 = 807
utils.checkList([7, 0, 8], utils.listToArray(t.addTwoNumbers(utils.listFromArray([2, 4, 3]), utils.listFromArray([5, 6, 4]))))
# 342 + 58 = 400
utils.checkList([0, 0, 4], utils.listToArray(t.addTwoNumbers(utils.listFromArray([2, 4, 3]), utils.listFromArray([8, 5]))))
# 342 + 767 = 1109
utils.checkList([9, 0, 1, 1], utils.listToArray(t.addTwoNumbers(utils.listFromArray([2, 4, 3]), utils.listFromArray([7, 6, 7]))))
# 0 + 58 = 58
utils.checkList([8, 5], utils.listToArray(t.addTwoNumbers(utils.listFromArray([0]), utils.listFromArray([8, 5]))))
# 1 + 999 = 1000
utils.checkList([0, 0, 0, 1], utils.listToArray(t.addTwoNumbers(utils.listFromArray([1]), utils.listFromArray([9, 9, 9]))))
# 2 + 999 = 1001
utils.checkList([1, 0, 0, 1], utils.listToArray(t.addTwoNumbers(utils.listFromArray([2]), utils.listFromArray([9, 9, 9]))))