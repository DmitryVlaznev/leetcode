# 298. Binary Tree Longest Consecutive Sequence

# Medium

# Given the root of a binary tree, return the length of the longest
# consecutive sequence path.

# The path refers to any sequence of nodes from some starting node to
# any node in the tree along the parent-child connections. The longest
# consecutive path needs to be from parent to child (cannot be the
# reverse).


# Example 1:
# Input: root = [1,null,3,2,4,null,null,null,5]
# Output: 3
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

# Example 2:
# Input: root = [2,null,3,2,null,1]
# Output: 2
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so
# return 2.


# Constraints:
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -3 * 10^4 <= Node.val <= 3 * 10^4

from typing import Optional
from utils import TreeNode


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 1

        def dfs(start, end, node):
            nonlocal res

            if node.val == end + 1:
                end += 1
            else:
                start = end = node.val
            res = max(res, end - start + 1)
            if node.left:
                dfs(start, end, node.left)
            if node.right:
                dfs(start, end, node.right)

        dfs(float("-inf"), float("-inf"), root)
        return res