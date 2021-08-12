# 1168. Optimize Water Distribution in a Village

# Hard

# There are n houses in a village. We want to supply water for all the
# houses by building wells and laying pipes.

# For each house i, we can either build a well inside it directly with
# cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water
# from another well to it. The costs to lay pipes between houses are
# given by the array pipes, where each pipes[j] = [house1j, house2j,
# costj] represents the cost to connect house1j and house2j together
# using a pipe. Connections are bidirectional.

# Return the minimum total cost to supply water to all houses.


# Example 1:
# Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
# Output: 3
# Explanation:
# The image shows the costs of connecting houses using pipes.
# The best strategy is to build a well in the first house with cost 1
# and connect the other houses to it with cost 2 so the total cost is 3.

# Constraints:
# 1 <= n <= 10^4
# wells.length == n
# 0 <= wells[i] <= 10^5
# 1 <= pipes.length <= 10^4
# pipes[j].length == 3
# 1 <= house1j, house2j <= n
# 0 <= costj <= 10^5
# house1j != house2j

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: List[int], pipes: List[List[int]]
    ) -> int:
        graph = defaultdict(list)

        for index, cost in enumerate(wells):
            graph[0].append((cost, index + 1))

        for house_1, house_2, cost in pipes:
            graph[house_1].append((cost, house_2))
            graph[house_2].append((cost, house_1))
        mst_set = set([0])

        heapq.heapify(graph[0])
        edges_heap = graph[0]

        res = 0
        while len(mst_set) < n + 1:
            cost, next_house = heapq.heappop(edges_heap)
            if next_house not in mst_set:
                mst_set.add(next_house)
                res += cost
                for new_cost, neighbor_house in graph[next_house]:
                    if neighbor_house not in mst_set:
                        heapq.heappush(edges_heap, (new_cost, neighbor_house))
        return res