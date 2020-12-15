# 382. Linked List Random Node

# Medium

# Given a singly linked list, return a random node's value from the
# linked list. Each node must have the same probability of being chosen.

# Follow up:
# What if the linked list is extremely large and its length is unknown
# to you? Could you solve this efficiently without using extra space?

# Example:
# Init a singly linked list [1,2,3].

# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);

# getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
# solution.getRandom();

from utils import ListNode, listFromArray


class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        from random import random

        k, res, p = 1, 0, self.head
        while p:
            if 1 / k >= random():
                res = p.val
            p = p.next
            k += 1
        return res


# Your Solution object will be instantiated and called as such:
t = Solution(listFromArray([1, 2]))
print(t.getRandom())
print(t.getRandom())
print(t.getRandom())
print(t.getRandom())
print(t.getRandom())
print(t.getRandom())
print(t.getRandom())
print(t.getRandom())