# 1361. Validate Binary Tree Nodes

# Medium

# You have n binary tree nodes numbered from 0 to n - 1 where node i has
# two children leftChild[i] and rightChild[i], return true if and only
# if all the given nodes form exactly one valid binary tree.

# If node i has no left child then leftChild[i] will equal -1, similarly
# for the right child.

# Note that the nodes have no values and that we only use the node
# numbers in this problem.

# Example 1:
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true

# Example 2:
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false

# Example 3:
# Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
# Output: false


# Constraints:
# n == leftChild.length == rightChild.length
# 1 <= n <= 10^4
# -1 <= leftChild[i], rightChild[i] <= n - 1

from typing import List


class UnionFind:
    def __init__(self, size):
        self.parents = list(range(size))

    def union(self, parent, child):
        self.parents[self.root(child)] = self.parents[self.root(parent)]

    def root(self, a):
        while self.parents[a] != a:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        uf = UnionFind(n)
        has_parent = set()
        for i in range(n):
            if leftChild[i] != -1:
                if leftChild[i] in has_parent:
                    return False
                uf.union(i, leftChild[i])
                has_parent.add(leftChild[i])
            if rightChild[i] != -1:
                if rightChild[i] in has_parent:
                    return False
                uf.union(i, rightChild[i])
                has_parent.add(rightChild[i])

        parents = set([uf.root(i) for i in range(n)])
        if len(parents) > 1:
            return False

        return len(has_parent) == n - 1


s = Solution()
# s.validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, -1, -1, -1])
# s.validateBinaryTreeNodes(4, [3, -1, 1, -1], [-1, -1, 0, -1])
s.validateBinaryTreeNodes(3, [1, -1, -1], [-1, -1, 1])
