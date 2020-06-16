# 210. Course Schedule II

# There are a total of n courses you have to take, labeled from 0 to
# n-1.

# Some courses may have prerequisites, for example to take course 0 you
# have to first take course 1, which is expressed as a pair: [0,1]

# return the ordering of courses you should take to finish all courses.
# Given the total number of courses and a list of prerequisite pairs,

# There may be multiple correct orders, you just need to return one of
# them. If it is impossible to finish all courses, return an empty
# array.

# Example 1:
# Input: 2, [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
#              course 0. So the correct course order is [0,1] .

# Example 2:
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

from typing import List


class Solution:
    def dfs(self, graph, stack, visited, node):
        visited[node] = 1
        for n in graph[node]:
            if visited[n] == 1:
                raise Exception()
            if visited[n] == 0:
                self.dfs(graph, stack, visited, n)
        visited[node] = 2
        stack.append(node)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for n in range(numCourses)]
        for edge in prerequisites: graph[edge[1]].append(edge[0])
        visited = [0] * numCourses
        stack = []
        rest = set(range(0, numCourses))

        try:
            while rest:
                node = rest.pop()
                if visited[node] == 0:
                    self.dfs(graph, stack, visited, node)
            stack.reverse()
            return stack
        except:
            return []

# print("cycle detected!!!")
# print(">>> node", node, "stack", stack[:])
t = Solution()
print("[0, 1] = ", t.findOrder(2, [[1,0]]))
print("[0, 1, 2, 3] or [0, 2, 1, 3] = ", t.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print("[] = ", t.findOrder(3, [[1,0],[2,1],[0,2]]))
print("[5, 6, 4, 0, 2, 1, 3] = ", t.findOrder(7, [[1,0],[2,0],[3,1],[3,2],[2,4],[6,5]]))
print("[0, 1] or [1, 0] = ", t.findOrder(2, []))
print("[] = ", t.findOrder(0, []))