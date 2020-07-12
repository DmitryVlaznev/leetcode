# 430. Flatten a Multilevel Doubly Linked List

# You are given a doubly linked list which in addition to the next and
# previous pointers, it could have a child pointer, which may or may not
# point to a separate doubly linked list. These child lists may have one
# or more children of their own, and so on, to produce a multilevel data
# structure, as shown in the example below.

# Flatten the list so that all the nodes appear in a single-level,
# doubly linked list. You are given the head of the first level of the
# list.

# Example 1:
# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
# Explanation:
# The multilevel linked list in the input is as follows:

# Example 2:
# Input: head = [1,2,null,3]
# Output: [1,3,2]
# Explanation:
# The input multilevel linked list is as follows:

#   1---2---NULL
#   |
#   3---NULL

# Example 3:
# Input: head = []
# Output: []

# How multilevel linked list is represented in test case:
# We use the multilevel linked list from Example 1 above:
#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL
# The serialization of each level is as follows:


# [1,2,3,4,5,6,null]
# [7,8,9,10,null]
# [11,12,null]

# To serialize all levels together we will add nulls in each level to
# signify no node connects to the upper node of the previous level. The
# serialization becomes:

# [1,2,3,4,5,6,null]
# [null,null,7,8,9,10,null]
# [null,11,12,null]

# Merging the serialization of each level and removing trailing nulls we
# obtain:

# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

# Constraints:

# Number of Nodes will not exceed 1000.
# 1 <= Node.val <= 10^5

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def children(self, root):
        p = tail = root
        while p:
            q = p.next
            tail = p.next if p.next else p
            if p.child:
                r, tail = self.children(p.child)
                p.next = r
                r.prev = p
                tail.next = q
                if q: q.prev = tail
            p.child = None
            p = q
        return root, tail

    def flatten(self, head: 'Node') -> 'Node':
        self.children(head)
        return head

def toArray(head: Node) -> List:
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    return arr

def log(correct, res):
    if len(correct) == len(res) and "".join(str(s) for s in correct) == "".join(str(s) for s in res):
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


# 1 - null
# |
# 2 - null
# |
# ...
# |
# 10 - null
last = Node(10, None, None, None)
for i in range(9, 0, -1):
    last = Node(i, None, None, last)
t = Solution()
log([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], toArray(t.flatten(last)))

# 11 - 12 - null
#  |
# 21 - 22 - 23 - 24 - 25 - null
#            |
#           31 - 32 - null
#            |
#           41 - null
l4 = Node(41, None, None, None)
l3 = Node(32, None, None, None)
l3 = Node(31, None, l3, l4)
l2 = Node(25, None, None, None)
l2 = Node(24, None, l2, None)
l2 = Node(23, None, l2, l3)
l2 = Node(22, None, l2, None)
l2 = Node(21, None, l2, None)
l1 = Node(12, None, None, None)
l1 = Node(11, None, l1, l2)
t = Solution()
log([11, 21, 22, 23, 31, 41,  32 , 24, 25, 12], toArray(t.flatten(l1)))