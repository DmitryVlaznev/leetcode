# 1192. Critical Connections in a Network

# Hard

# There are n servers numbered from 0 to n-1 connected by undirected
# server-to-server connections forming a network where connections[i] =
# [a, b] represents a connection between servers a and b. Any server can
# reach any other server directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some
# server unable to reach some other server.

# Return all critical connections in the network in any order.

# Example 1:
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.

# Constraints:
# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
# There are no repeated connections.

from typing import List
from collections import defaultdict


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        seen, ranks, back_ranks, res = [False] * n, [-1] * n, [-1] * n, []
        self.current_rank = 0
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent=-1):
            seen[node] = True
            self.current_rank += 1
            ranks[node] = back_ranks[node] = self.current_rank
            for child in graph[node]:
                if child == parent:
                    continue
                elif seen[child]:
                    back_ranks[node] = min(ranks[child], back_ranks[node])
                else:
                    dfs(child, node)
                    back_ranks[node] = min(back_ranks[node], back_ranks[child])
                    if back_ranks[child] > ranks[node]:
                        res.append([node, child])

        for i in range(n):
            if not seen[i]:
                dfs(i)

        return res