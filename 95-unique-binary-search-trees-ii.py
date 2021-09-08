# 95. Unique Binary Search Trees II

# Medium

# Given an integer n, return all the structurally unique BST's (binary
# search trees), which has exactly n nodes of unique values from 1 to n.
# Return the answer in any order.

# Example 1:
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# Constraints:
# 1 <= n <= 8

from typing import List, Optional, Tuple
from utils import TreeNode
from functools import lru_cache


class Solution:
    c = 0

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.c = 0

        @lru_cache(maxsize=None)
        def subtrees(values: Tuple[int]) -> List[Optional[TreeNode]]:
            self.c += 1

            if not values:
                return [None]
            if len(values) == 1:
                return [TreeNode(values[0])]

            res = []
            for i in range(len(values)):
                left = subtrees(values[0:i])
                right = subtrees(values[i + 1 :])

                for l in left:
                    for r in right:
                        res.append(TreeNode(values[i], l, r))
            return res

        return subtrees(tuple([i + 1 for i in range(n)]))


s = Solution()
s.generateTrees(3)
print("3 =>>", s.c)
s.generateTrees(5)
print("5 =>>", s.c)
s.generateTrees(8)
print("8 =>>", s.c)
