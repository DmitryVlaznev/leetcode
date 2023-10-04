# 1615. Maximal Network Rank

# Medium

# There is an infrastructure of n cities with some number of roads
# connecting these cities. Each roads[i] = [ai, bi] indicates that there
# is a bidirectional road between cities ai and bi.

# The network rank of two different cities is defined as the total
# number of directly connected roads to either city. If a road is
# directly connected to both cities, it is only counted once.

# The maximal network rank of the infrastructure is the maximum network
# rank of all pairs of different cities.

# Given the integer n and the array roads, return the maximal network
# rank of the entire infrastructure.


# Example 1:
# Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# Output: 4
# Explanation: The network rank of cities 0 and 1 is 4 as there are 4
# roads that are connected to either 0 or 1. The road between 0 and 1 is
# only counted once.

# Example 2:
# Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# Output: 5
# Explanation: There are 5 roads that are connected to cities 1 or 2.

# Example 3:
# Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
# Output: 5
# Explanation: The network rank of 2 and 5 is 5. Notice that all the
# cities do not have to be connected.


# Constraints:

# 2 <= n <= 100
# 0 <= roads.length <= n * (n - 1) / 2
# roads[i].length == 2
# 0 <= ai, bi <= n-1
# ai != bi
# Each pair of cities has at most one road connecting them.

from typing import List
from utils import checkValue


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [[_] for _ in range(n)]

        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        import functools

        def comparator(a, b):
            return len(a) - len(b)

        graph.sort(key=functools.cmp_to_key(comparator))
        graph.reverse()

        f_max, f_max_count, i = len(graph[0]), 1, 1
        while i < len(graph) and len(graph[i]) == f_max:
            f_max_count, i = f_max_count + 1, i + 1

        if f_max_count > 1:
            res = 0
            for i in range(f_max_count):
                for j in range(f_max_count):
                    if i == j:
                        continue
                    rank = len(graph[i]) + len(graph[j]) - 2
                    if graph[j][0] in graph[i]:
                        rank -= 1
                    res = max(res, rank)
            return res

        s_max, s_max_count, i = len(graph[i]), 1, i + 1
        while i < len(graph) and len(graph[i]) == s_max:
            s_max_count, i = s_max_count + 1, i + 1

        res = 0
        for j in range(1, s_max_count + 1):
            rank = len(graph[0]) + len(graph[j]) - 2
            if graph[j][0] in graph[0]:
                rank -= 1
            res = max(res, rank)
        return res


t = Solution()

checkValue(2, t.maximalNetworkRank(3, [[0, 2], [0, 1]]))
# checkValue(0, t.maximalNetworkRank(2, []))
# checkValue(4, t.maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]]))
# checkValue(5, t.maximalNetworkRank(5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]))
# checkValue(5, t.maximalNetworkRank(8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]))
