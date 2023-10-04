# 1584. Min Cost to Connect All Points

# Medium

# You are given an array points representing integer coordinates of some
# points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the
# manhattan distance between them: |xi - xj| + |yi - yj|, where |val|
# denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are
# connected if there is exactly one simple path between any two points.


# Example 1:
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.

# Example 2:
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18


# Constraints:

# 1 <= points.length <= 1000
# -10^6 <= xi, yi <= 10^6
# All pairs (xi, yi) are distinct.

from typing import List


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]

    def find(self, v):
        while self.parents[v] != v:
            self.parents[v] = self.parents[self.parents[v]]
            v = self.parents[v]
        return v

    def union(self, a, b):
        self.parents[self.find(a)] = self.find(b)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        return self.primOptimized(points)

    def distance(self, p, q):
        return abs(p[0] - q[0]) + abs(p[1] - q[1])

    def prim(self, points: List[List[int]]) -> int:
        import heapq

        added, edges = set(), []

        def add_node_edges(n):
            for i in range(len(points)):
                if i != n and i not in added:
                    heapq.heappush(edges, (self.distance(points[n], points[i]), i))

        added.add(0)
        add_node_edges(0)
        res = 0
        while len(added) < len(points):
            d, i = heapq.heappop(edges)
            if i in added:
                continue
            res += d
            added.add(i)
            add_node_edges(i)
        return res

    def primOptimized(self, points: List[List[int]]) -> int:
        added, shortest_edges = set(), [float("inf")] * len(points)

        def update_shortest_edges(n):
            for i in range(len(points)):
                if i != n and i not in added:
                    d = self.distance(points[n], points[i])
                    shortest_edges[i] = (
                        shortest_edges[i] if shortest_edges[i] <= d else d
                    )

        added.add(0)
        shortest_edges[0] = 0
        update_shortest_edges(0)
        res = 0
        while len(added) < len(points):
            n, d = -1, float("inf")
            for i in range(len(points)):
                if i == n or i in added:
                    continue
                if shortest_edges[i] < d:
                    n, d = i, shortest_edges[i]
            res += d
            added.add(n)
            update_shortest_edges(n)
        return res

    def kruskal(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                edges.append((self.distance(points[i], points[j]), i, j))
        edges.sort(key=lambda e: e[0])

        uf, res, connections = UnionFind(len(points)), 0, 0
        for l, i, j in edges:
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                res, connections = res + l, connections + 1
                if connections == len(points) - 1:
                    return res


from utils import checkValue

s = Solution()
checkValue(20, s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
checkValue(53, s.minCostConnectPoints([[2, -3], [-17, -8], [13, 8], [-17, -15]]))
checkValue(18, s.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))
