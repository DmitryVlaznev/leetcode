# 305. Number of Islands II

# Hard

# You are given an empty 2D binary grid grid of size m x n. The grid
# represents a map where 0's represent water and 1's represent land.
# Initially, all the cells of grid are water cells (i.e., all the cells
# are 0's).

# We may perform an add land operation which turns the water at position
# into a land. You are given an array positions where positions[i] =
# [ri, ci] is the position (ri, ci) at which we should operate the ith
# operation.

# Return an array of integers answer where answer[i] is the number of
# islands after turning the cell (ri, ci) into a land.

# An island is surrounded by water and is formed by connecting adjacent
# lands horizontally or vertically. You may assume all four edges of the
# grid are all surrounded by water.


# Example 1:
# Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
# Output: [1,1,2,3]
# Explanation:
# Initially, the 2d grid is filled with water.
# - Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
# - Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
# - Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
# - Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.

# Example 2:
# Input: m = 1, n = 1, positions = [[0,0]]
# Output: [1]

# Constraints:
# 1 <= m, n, positions.length <= 10^4
# 1 <= m * n <= 10^4
# positions[i].length == 2
# 0 <= ri < m
# 0 <= ci < n

# Follow up: Could you solve it in time complexity O(k log(mn)), where k == positions.length?

from typing import List


class UnionFind:
    def __init__(self, size):
        self.parents = list(range(size))

    def union(self, a, b):
        self.parents[self.find(a)] = self.parents[self.find(b)]

    def find(self, a):
        while self.parents[a] != a:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def idx(x, y):
            nonlocal n
            return x * n + y

        land, islands, uf, res = set(), 0, UnionFind(m * n), []
        for x, y in positions:
            if idx(x, y) in land:
                res.append(islands)
                continue
            islands += 1
            land.add(idx(x, y))
            d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in d:
                if x + dx < 0 or x + dx >= m or y + dy < 0 or y + dy >= n:
                    continue
                if idx(x + dx, y + dy) in land and uf.find(idx(x, y)) != uf.find(
                    idx(x + dx, y + dy)
                ):
                    uf.union(idx(x + dx, y + dy), idx(x, y))
                    islands -= 1
            res.append(islands)
        return res


s = Solution()
s.numIslands2(1, 2, [[0, 1], [0, 0]])
