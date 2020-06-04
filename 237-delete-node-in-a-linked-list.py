# 237. Delete Node in a Linked List

# Write a function to delete a node (except the tail) in a singly linked
# list, given only access to that node.

# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked
# list should become 4 -> 1 -> 9 after calling your function.

# Example 2:
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked
# list should become 4 -> 5 -> 9 after calling your function.

# Note:
# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node
# of the linked list.

# Do not return anything from your function.

from typing import List


# Definition for singly-linked list.
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

    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

def log(correct, res):
    if len(correct) == len(res) and set(correct) == set(res): print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

l = t.fromArray([4,5,1,9])
t.deleteNode(l.next)
log([4,1,9], t.toArray(l))

l = t.fromArray([4,5,1,9])
t.deleteNode(l.next.next)
log([4,5,9], t.toArray(l))

l = t.fromArray([4,5])
t.deleteNode(l)
log([5], t.toArray(l))

