# 1290. Convert Binary Number in a Linked List to Integer

# Given head which is a reference node to a singly-linked list. The
# value of each node in the linked list is either 0 or 1. The linked
# list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# Example 1:
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Example 2:
# Input: head = [0]
# Output: 0

# Example 3:
# Input: head = [1]
# Output: 1

# Example 4:
# Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
# Output: 18880

# Example 5:
# Input: head = [0,0]
# Output: 0


# Constraints:
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from utils import ListNode, listFromArray, checkValue


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        p = head
        while p:
            if p.val:
                res = res | 1
            p = p.next
            if p:
                res = res << 1
        return res


t = Solution()
checkValue(5, t.getDecimalValue(listFromArray([1, 0, 1])))
checkValue(0, t.getDecimalValue(listFromArray([0])))
checkValue(1, t.getDecimalValue(listFromArray([1])))
checkValue(
    18880,
    t.getDecimalValue(listFromArray([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])),
)
checkValue(0, t.getDecimalValue(listFromArray([0, 0])))
