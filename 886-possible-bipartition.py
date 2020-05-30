# 886. Possible Bipartition

# Given a set of N people (numbered 1, 2, ..., N), we would like to
# split everyone into two groups of any size.

# Each person may dislike some other people, and they should not go into
# the same group.

# Formally, if dislikes[i] = [a, b], it means it is not allowed to put
# the people numbered a and b into the same group.

# Return true if and only if it is possible to split everyone into two
# groups in this way.

# Example 1:
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]

# Example 2:
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false

# Example 3:
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false

# Note:
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].

from typing import List


class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not len(dislikes): return True

        graph = [[] for n in range(N + 1)]
        for edge in dislikes:
            graph[edge[0]].append(edge)
            graph[edge[1]].append(edge)

        from collections import deque
        colors = [-1] * (N + 1)
        rest = set(range(1, N + 1))
        queue = deque()
        while rest or queue:
            if not len(queue):
                node = rest.pop()
                colors[node] = 0
                queue.append(node)

            cur = queue.popleft()
            cc = colors[cur]
            nc = 1 - cc
            for edge in graph[cur]:
                node = edge[0] if edge[0] != cur else edge[1]
                if colors[node] == -1:
                    colors[node] = nc
                    queue.append(node)
                    rest.remove(node)
                elif colors[node] == cc: return False
        return True

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(False, t.possibleBipartition(5, [[1,2],[3,4],[4,5],[3,5]]))

log(True, t.possibleBipartition(4, [[1,2],[1,3],[2,4]]))
log(False, t.possibleBipartition(3, [[1,2],[1,3],[2,3]]))
log(False, t.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))
log(True, t.possibleBipartition(8, [[1,2],[2,7],[1,3],[3,4],[4,5],[5,6],[5,7],[6,8],[7,8]]))
log(True, t.possibleBipartition(3, [[1,2]]))
log(True, t.possibleBipartition(3, []))