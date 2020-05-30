# 207. Course Schedule

# There are a total of numCourses courses you have to take, labeled from
# 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you
# have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is
# it possible for you to finish all courses?

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.


# Constraints:
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5

from typing import List


class Solution:

    def mark(self, graph, rest, visited, node):
        children = graph[node]
        for c in children:
            if visited[c] == 1: return True
            if visited[c] == 2: continue
            visited[c] = 1
            if self.mark(graph, rest, visited, c): return True
            visited[c] = 2
            rest.remove(c)
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for n in range(numCourses)]
        for edge in prerequisites: graph[edge[1]].append(edge[0])
        visited = [0] * numCourses
        rest = set(range(0, numCourses))

        while rest:
            node = rest.pop()
            visited[node] = 1
            if self.mark(graph, rest, visited, node): return False
            visited[node] = 2
        return True

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(True, t.canFinish(2, [[1,0]]))
log(True, t.canFinish(2, [[0,1]]))
log(False, t.canFinish(2, [[1,0],[0,1]]))
log(True, t.canFinish(17, [[2,1],[3,1],[4,2],[4,3],[5,4],[11,10],[12,10],[15,11]]))
log(False, t.canFinish(17, [[2,1],[3,1],[4,2],[4,3],[5,4],[11,10],[12,10],[15,11],[11,5],[3,15]]))