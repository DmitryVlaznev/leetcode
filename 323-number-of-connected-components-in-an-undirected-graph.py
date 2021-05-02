# 323. Number of Connected Components in an Undirected Graph

# Medium

# You have a graph of n nodes. You are given an integer n and an array
# edges where edges[i] = [ai, bi] indicates that there is an edge
# between ai and bi in the graph.

# Return the number of connected components in the graph.

# Example 1:
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

# Example 2:
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1

# Constraints:
# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()

        graph = [[] for _ in range(n)]
        for fr, to in edges:
            graph[fr].append(to)
            graph[to].append(fr)

        def dfs(start):
            for node in graph[start]:
                if node not in seen:
                    seen.add(node)
                    dfs(node)

        res = 0
        for i in range(n):
            if i not in seen:
                res += 1
                dfs(i)
        return res
