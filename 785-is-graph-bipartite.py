# 785. Is Graph Bipartite?

# Medium

# Given an undirected graph, return true if and only if it is bipartite.

# Recall that a graph is bipartite if we can split its set of nodes into
# two independent subsets A and B, such that every edge in the graph has
# one node in A and another node in B.

# The graph is given in the following form: graph[i] is a list of
# indexes j for which the edge between nodes i and j exists. Each node
# is an integer between 0 and graph.length - 1. There are no self edges
# or parallel edges: graph[i] does not contain i, and it doesn't contain
# any element twice.

# Example 1:
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can divide the vertices into two groups: {0, 2} and
# {1, 3}.

# Example 2:
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: We cannot find a way to divide the set of nodes into two
# independent subsets.

# Constraints:
# 1 <= graph.length <= 100
# 0 <= graph[i].length < 100
# 0 <= graph[i][j] <= graph.length - 1
# graph[i][j] != i
# All the values of graph[i] are unique.
# The graph is guaranteed to be undirected.

from typing import List
from utils import checkValue
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True
        seen = [None] * len(graph)
        dq = deque()
        seen[0], p = 0, 1
        dq.append(0)
        while dq:
            l = len(dq)
            while l:
                l -= 1
                node = dq.popleft()
                color = 0 if seen[node] else 1
                for sibling in graph[node]:
                    if seen[sibling] is None:
                        seen[sibling] = color
                        dq.append(sibling)
                    elif seen[sibling] != color:
                        return False
            if not dq:
                while p < len(graph) and seen[p] is not None:
                    p += 1
                if p < len(graph):
                    seen[p] = 0
                    dq.append(p)
        return True


t = Solution()

checkValue(True, t.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
checkValue(False, t.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
checkValue(True, t.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2], [5], [4, 6], [5]]))
checkValue(
    False, t.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2], [5, 6], [4, 6], [4, 5]])
)
checkValue(True, t.isBipartite([[], []]))
checkValue(True, t.isBipartite([[]]))
checkValue(True, t.isBipartite([]))
