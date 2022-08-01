# 1182. Shortest Distance to Target Color

# Medium

# You are given an array colors, in which there are three colors: 1, 2
# and 3.

# You are also given some queries. Each query consists of two integers i
# and c, return the shortest distance between the given index i and the
# target color c. If there is no solution return -1.


# Example 1:
# Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
# Output: [3,0,3]
# Explanation:
# The nearest 3 from index 1 is at index 4 (3 steps away).
# The nearest 2 from index 2 is at index 2 itself (0 steps away).
# The nearest 1 from index 6 is at index 3 (3 steps away).

# Example 2:
# Input: colors = [1,2], queries = [[0,3]]
# Output: [-1]
# Explanation: There is no 3 in the array.


# Constraints:
# 1 <= colors.length <= 5*10^4
# 1 <= colors[i] <= 3
# 1 <= queries.length <= 5*10^4
# queries[i].length == 2
# 0 <= queries[i][0] < colors.length
# 1 <= queries[i][1] <= 3

from typing import List


class Solution:
    def shortestDistanceColor(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:
        distance = [[float("inf")] * 3 for _ in range(len(colors))]

        cur = [float("inf")] * 3
        for i in range(len(colors)):
            c = colors[i] - 1
            cur[c] = i
            distance[i][0] = i - cur[0] if cur[0] != float("inf") else float("inf")
            distance[i][1] = i - cur[1] if cur[1] != float("inf") else float("inf")
            distance[i][2] = i - cur[2] if cur[2] != float("inf") else float("inf")

        cur = [float("inf")] * 3
        for i in range(len(colors) - 1, -1, -1):
            c = colors[i] - 1
            cur[c] = i
            distance[i][0] = min(distance[i][0], cur[0] - i)
            distance[i][1] = min(distance[i][1], cur[1] - i)
            distance[i][2] = min(distance[i][2], cur[2] - i)
        print(distance)
        res = []
        for i, c in queries:
            res.append(distance[i][c - 1] if distance[i][c - 1] != float("inf") else -1)

        return res


s = Solution()
print(s.shortestDistanceColor([1, 1, 2, 1, 3, 2, 2, 3, 3], [[1, 3], [2, 2], [6, 1]]))
print(s.shortestDistanceColor([1, 2], [[0, 3]]))
