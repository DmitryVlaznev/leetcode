# 199. Binary Tree Right Side View

# Medium

# Given a binary tree, imagine yourself standing on the right side of
# it, return the values of the nodes you can see ordered from top to
# bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

from typing import List
from utils import TreeNode, checkList, treeFromArray


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        from collections import deque

        dq, res = deque(), []
        dq.append(root)
        while dq:
            l = len(dq)
            while l:
                node = dq.popleft()
                if l == 1:
                    res.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                l -= 1
        return res


t = Solution()

checkList([1, 3, 4], t.rightSideView(treeFromArray([1, 2, 3, None, 5, None, 4], 0)))
checkList([1, 3, 6], t.rightSideView(treeFromArray([1, 2, 3, None, 5, 6], 0)))
