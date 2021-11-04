# 437. Path Sum III

# Given the root of a binary tree and an integer targetSum, return the
# number of paths where the sum of the values along the path equals
# targetSum.

# The path does not need to start or end at the root or a leaf, but it
# must go downwards (i.e., traveling only from parent nodes to child
# nodes).

# Example 1:
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.

# Example 2:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3

# Constraints:
# The number of nodes in the tree is in the range [0, 1000].
# -10^9 <= Node.val <= 10^9
# -1000 <= targetSum <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
from utils import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        res, hash = 0, defaultdict(lambda: 0)

        def dfs(node, cur_sum):
            nonlocal res, sum

            if not node:
                return

            cur_sum += node.val
            res += 1 if cur_sum == sum else 0
            res += hash[cur_sum - sum]
            hash[cur_sum] += 1
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
            hash[cur_sum] -= 1

        dfs(root, 0)
        return res
