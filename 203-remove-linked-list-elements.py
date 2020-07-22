# 203. Remove Linked List Elements
# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5


from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = None
        tail = None
        p = head
        while p:
            if p.val == val:
                if tail: tail.next = p.next
            else:
                if not res: res = p
                tail = p
            p = p.next
        return res


def log(correct, res):
    if len(correct) == len(res) and "".join(str(s) for s in correct) == "".join(str(s) for s in res):
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log([1,2,3,4,5], t.toArray(t.removeElements(t.fromArray([1,2,6,3,4,5,6]), 6)))
log([1,2,3,4,5], t.toArray(t.removeElements(t.fromArray([6,1,2,6,3,4,5,6]), 6)))
log([1,2,3,4,5], t.toArray(t.removeElements(t.fromArray([6,1,2,6,6,6,3,4,5,6]), 6)))
log([], t.toArray(t.removeElements(t.fromArray([6,6,6]), 6)))
log([], t.toArray(t.removeElements(t.fromArray([6,6]), 6)))
log([], t.toArray(t.removeElements(t.fromArray([6]), 6)))
log([], t.toArray(t.removeElements(t.fromArray([]), 6)))