# 117. Populating Next Right Pointers in Each Node II

# Medium

# Given a binary tree
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }

# Populate each next pointer to point to its next right node. If there
# is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Follow up:
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does
# not count as extra space for this problem.

# Example 1:
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function
# should populate each next pointer to point to its next right node,
# just like in Figure B. The serialized output is in level order as
# connected by the next pointers, with '#' signifying the end of each
# level.


# Constraints:
# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None

        from collections import deque

        dq = deque()
        dq.append(root)

        while dq:
            l = len(dq) - 1
            left_sibling = dq.popleft()
            if left_sibling.left:
                dq.append(left_sibling.left)
            if left_sibling.right:
                dq.append(left_sibling.right)
            while l:
                p = dq.popleft()
                if p.left:
                    dq.append(p.left)
                if p.right:
                    dq.append(p.right)
                left_sibling.next = p
                left_sibling = p
                l -= 1
        return root
