# 1214. Two Sum BSTs

# Medium

# Given the roots of two binary search trees, root1 and root2, return
# true if and only if there is a node in the first tree and a node in
# the second tree whose values sum up to a given integer target.

# Example 1:
# Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
# Output: true
# Explanation: 2 and 3 sum up to 5.

# Example 2:
# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
# Output: false

# Constraints:

# The number of nodes in each tree is in the range [1, 5000].
# -10^9 <= Node.val, target <= 10^9

from utils import TreeNode
from typing import Optional
from collections import deque


class Solution:
    def twoSumBSTs(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int
    ) -> bool:
        hash = set()

        def make_hash(node: Optional[TreeNode]):
            if not node:
                return
            hash.add(node.val)
            make_hash(node.left)
            make_hash(node.right)

        make_hash(root1)
        dq = deque()
        dq.append(root2)
        while dq:
            l = len(dq)
            while l:
                l -= 1
                node = dq.popleft()
                if (target - node.val) in hash:
                    return True
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return False
