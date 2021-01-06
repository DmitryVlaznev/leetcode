# 82 Remove Duplicates from Sorted List II

# Medium

# Given the head of a sorted linked list, delete all nodes that have
# duplicate numbers, leaving only distinct numbers from the original
# list. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Example 2:
# Input: head = [1,1,1,2,3]
# Output: [2,3]


# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
from typing import List
from utils import listFromArray, listToArray, checkList, ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        h, t, p = None, None, head
        while p:
            if not p.next or p.val != p.next.val:
                if t:
                    t.next = p
                    t = p
                else:
                    h = t = p
                p = p.next
                t.next = None
            else:
                v = p.val
                while p and p.val == v:
                    p = p.next
        return h


t = Solution()

checkList(
    [1, 2, 5], listToArray(t.deleteDuplicates(listFromArray([1, 2, 3, 3, 4, 4, 5])))
)

checkList([2, 3], listToArray(t.deleteDuplicates(listFromArray([1, 1, 1, 2, 3]))))
checkList([], listToArray(t.deleteDuplicates(listFromArray([1, 1, 1]))))
checkList([2], listToArray(t.deleteDuplicates(listFromArray([2, 3, 3, 3]))))
checkList([1], listToArray(t.deleteDuplicates(listFromArray([1]))))
