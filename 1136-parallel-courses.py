# 1136. Parallel Courses

# Medium

# You are given an integer n which indicates that we have n courses,
# labeled from 1 to n. You are also given an array relations where
# relations[i] = [a, b], representing a prerequisite relationship
# between course a and course b: course a has to be studied before
# course b.

# In one semester, you can study any number of courses as long as you
# have studied all the prerequisites for the course you are studying.

# Return the minimum number of semesters needed to study all courses. If
# there is no way to study all the courses, return -1.

# Example 1:
# Input: n = 3, relations = [[1,3],[2,3]]
# Output: 2
# Explanation: In the first semester, courses 1 and 2 are studied. In
# the second semester, course 3 is studied.

# Example 2:
# Input: n = 3, relations = [[1,2],[2,3],[3,1]]
# Output: -1
# Explanation: No course can be studied because they depend on each
# other.


# Constraints:
# 1 <= n <= 5000
# 1 <= relations.length <= 5000
# 1 <= a, b <= n
# a != b
# All the pairs [a, b] are unique.

from typing import List
from utils import checkValue


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        from collections import defaultdict

        graph = defaultdict(list)
        for s, d in relations:
            graph[s].append(d)

        visited = {}

        def dfs(s: int) -> int:
            if s in visited:
                return visited[s]

            visited[s] = -1
            max_len = 1
            for d in graph[s]:
                d_len = dfs(d)
                if d_len == -1:
                    return -1
                max_len = d_len + 1 if d_len + 1 > max_len else max_len
            visited[s] = max_len
            return visited[s]

        max_len = 0
        for d in range(n):
            d_len = dfs(d)
            if d_len == -1:
                return -1
            max_len = d_len if d_len > max_len else max_len
        return max_len

    def minimumSemesters2(self, n: int, relations: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        r_graph = [[] for _ in range(n + 1)]
        for fr, to in relations:
            graph[fr].append(to)
            r_graph[to].append(fr)

        # cycle detection
        grey, black, stack = set(), set(), []

        def t_sort(p, d):
            grey.add(p)
            for c in graph[p]:
                if c in grey:
                    return True
                elif c not in black:
                    if t_sort(c, d + 1):
                        return True
            grey.remove(p)
            black.add(p)
            stack.append(p)
            return False

        for p in range(1, n + 1):
            if p not in black:
                if t_sort(p, 1):
                    return -1

        # find distance
        dist = [1] * (n + 1)
        while stack:
            p = stack.pop()
            if r_graph[p]:
                dist[p] = max(dist[c] + 1 for c in r_graph[p])

        return max(dist)


t = Solution()

checkValue(2, t.minimumSemesters(3, [[1, 3], [2, 3]]))
checkValue(2, t.minimumSemesters(5, [[1, 3], [2, 3], [4, 5]]))
checkValue(
    5,
    t.minimumSemesters(
        7, [[6, 1], [1, 5], [7, 5], [7, 3], [1, 2], [5, 4], [2, 4], [4, 3]]
    ),
)
checkValue(-1, t.minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]))
checkValue(1, t.minimumSemesters(3, []))
