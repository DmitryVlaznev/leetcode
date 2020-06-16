# 787. Cheapest Flights Within K Stops

# There are n cities connected by m flights. Each flight starts from
# city u and arrives at v with a price w.

# Now given all the cities and flights, together with starting city src
# and the destination dst, your task is to find the cheapest price from
# src to dst with up to k stops. If there is no such route, output -1.

# Example 1:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph looks like this:
# The cheapest price from city 0 to city 2 with at most 1 stop costs
# 200, as marked red in the picture.

# Example 2:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph looks like this:
# The cheapest price from city 0 to city 2 with at most 0 stop costs
# 500, as marked blue in the picture.


# Constraints:
# * The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# * The size of flights will be in range [0, n * (n - 1) / 2].
# * The format of each flight will be (src, dst, price).
# * The price of each flight will be in the range [1, 10000].
# * k is in the range of [0, n - 1].
# * There will not be any duplicated flights or self cycles.

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst: return 0
        graph = [[] for i in range(n)]
        for edge in flights: graph[edge[0]].append(edge)
        from collections import deque
        queue = deque()
        # node, len, steps
        queue.append((src, 0, 0, ))
        min_path = float("inf")

        while queue:
            node = queue.popleft()
            for edge in graph[node[0]]:
                if edge[1] == dst:
                    min_path = min(min_path, node[1] + edge[2])
                elif node[1] + edge[2] < min_path and node[2] < K:
                    queue.append((edge[1], node[1] + edge[2], node[2] + 1,))
        return min_path if min_path < float("inf") else -1

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(200, t.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
log(500, t.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))
log(140, t.findCheapestPrice(5, [[0,1,100],[1,2,100],[0,2,500],[0,3,10],[3,4,10],[4,1,20]], 0, 2, 3))
log(40, t.findCheapestPrice(5, [[0,1,100],[1,2,100],[0,2,500],[0,3,10],[3,4,10],[4,1,20]], 0, 1, 3))
log(40, t.findCheapestPrice(5, [[0,1,100],[1,2,100],[0,2,500],[0,3,10],[3,4,10],[4,1,20]], 0, 1, 2))
log(100, t.findCheapestPrice(5, [[0,1,100],[1,2,100],[0,2,500],[0,3,10],[3,4,10],[4,1,20]], 0, 1, 1))
log(-1, t.findCheapestPrice(5, [[0,1,100],[1,2,100],[0,2,500],[0,3,10],[3,4,10],[4,1,20]], 0, 4, 0))
log(0, t.findCheapestPrice(5, [[0,1,100],[1,2,100],[0,2,500],[0,3,10],[3,4,10],[4,1,20]], 0, 0, 0))
log(-1, t.findCheapestPrice(3, [[0,1,100]], 0, 2, 1))
log(-1, t.findCheapestPrice(3, [], 0, 2, 1))
log(0, t.findCheapestPrice(1, [], 0, 0, 1))

edges = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
log(47, t.findCheapestPrice(17, edges, 13, 4, 13))
