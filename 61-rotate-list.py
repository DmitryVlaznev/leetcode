# 61. Rotate List

# Given a linked list, rotate the list to the right by k places, where k
# is non-negative.

# Example 1:
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL

# Example 2:
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL

from utils import ListNode, listFromArray, listToArray, checkList

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        p = head
        l = 0
        while p:
            l += 1
            p = p.next
        if l < 2: return head
        delta = k % l
        if delta == 0: return head

        p = head
        while delta:
            delta -= 1
            p = p.next

        q = head
        while p.next:
            q = q.next
            p = p.next

        p.next = head
        head = q.next
        q.next = None
        return head

t = Solution()

checkList([4,5,1,2,3], listToArray(t.rotateRight(listFromArray([1,2,3,4,5]), 2)))
checkList([4,5,1,2,3], listToArray(t.rotateRight(listFromArray([1,2,3,4,5]), 12)))
checkList([1,2,3,4,5], listToArray(t.rotateRight(listFromArray([1,2,3,4,5]), 5)))
checkList([1,2], listToArray(t.rotateRight(listFromArray([1,2]), 10)))
checkList([2,1], listToArray(t.rotateRight(listFromArray([1,2]), 11)))
checkList([2], listToArray(t.rotateRight(listFromArray([2]), 11)))
checkList([2,0,1], listToArray(t.rotateRight(listFromArray([0,1,2]), 4)))