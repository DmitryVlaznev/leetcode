# 23. Merge k Sorted Lists

# You are given an array of k linked-lists lists, each linked-list is
# sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []

# Constraints:
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.

from typing import List
import utils

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        h = []
        for i, head in enumerate(lists):
            if head: heapq.heappush(h, (head.val, i, head))

        if not h: return None
        v, i, node = heapq.heappop(h)
        if node.next: heapq.heappush(h, (node.next.val, i, node.next))
        res = tail = ListNode(v)

        while h:
            v, i, node = heapq.heappop(h)
            if node.next: heapq.heappush(h, (node.next.val, i, node.next))
            tail.next = ListNode(v)
            tail = tail.next
        return res


t = Solution()

lists = [
    utils.listFromArray([1,4,5]),
    utils.listFromArray([1,3,4]),
    utils.listFromArray([2,6])
]
res = [1,1,2,3,4,4,5,6]
utils.checkList(res, utils.listToArray(t.mergeKLists(lists)))

utils.checkList([], utils.listToArray(t.mergeKLists([])))

utils.checkList([], utils.listToArray(t.mergeKLists([[]])))

lists = [
    utils.listFromArray([1]),
    utils.listFromArray([3]),
    utils.listFromArray([]),
    utils.listFromArray([2])
]
res = [1,2,3]
utils.checkList(res, utils.listToArray(t.mergeKLists(lists)))