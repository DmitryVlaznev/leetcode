# 1305. All Elements in Two Binary Search Trees

# Medium

# Given two binary search trees root1 and root2, return a list
# containing all the integers from both trees sorted in ascending order.


# Example 1:
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]

# Example 2:
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]


# Constraints:
# The number of nodes in each tree is in the range [0, 5000].
# -10^5 <= Node.val <= 10^5

from utils import TreeNode, treeFromArray, checkList
from typing import List


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def get_nodes(root: TreeNode):
            res, stack, seen = [], [root] if root else [], set()
            while stack:
                v = stack[-1]
                if v.left and v.left not in seen:
                    stack.append(v.left)
                    continue
                stack.pop()
                res.append(v.val)
                seen.add(v)
                if v.right:
                    stack.append(v.right)
            return res

        a, b = get_nodes(root1), get_nodes(root2)
        pa, pb, res = 0, 0, []
        while pa < len(a) or pb < len(b):
            na = a[pa] if pa < len(a) else float("inf")
            nb = b[pb] if pb < len(b) else float("inf")
            if na < nb:
                res.append(a[pa])
                pa += 1
            else:
                res.append(b[pb])
                pb += 1
        return res


s = Solution()

checkList(
    [0, 1, 1, 2, 3, 4],
    s.getAllElements(treeFromArray([2, 1, 4]), treeFromArray([1, 0, 3])),
)
checkList(
    [1, 1, 8, 8],
    s.getAllElements(treeFromArray([1, None, 8]), treeFromArray([8, 1])),
)