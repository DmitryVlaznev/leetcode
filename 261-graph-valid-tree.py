# 261. Graph Valid Tree

# Medium

# You have a graph of n nodes labeled from 0 to n - 1. You are given an
# integer n and a list of edges where edges[i] = [ai, bi] indicates that
# there is an undirected edge between nodes ai and bi in the graph.

# Return true if the edges of the given graph make up a valid tree, and
# false otherwise.

# Example 1:
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false

# Constraints:
# 1 <= 2000 <= n
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.

from typing import List
from collections import deque


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n < 2
        graph = [[] for _ in range(0, n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        seen = set()
        dq = deque()
        dq.append((edges[0][0], None))
        seen.add(edges[0][0])

        while dq:
            l = len(dq)
            while l:
                l -= 1
                cur, parent = dq.popleft()
                for child in graph[cur]:
                    if child == parent:
                        continue
                    if child in seen:
                        return False
                    seen.add(child)
                    dq.append((child, cur))
        return len(seen) == n