# 973. K Closest Points to Origin

# We have a list of points on the plane.  Find the K closest points to
# the origin (0, 0).

# (Here, the distance between two points on a plane is the Euclidean
# distance.)

# You may return the answer in any order.  The answer is guaranteed to
# be unique (except for the order that it is in.)

# Example 1:
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2:
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)

# Note:
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000

from typing import List


class Solution:
    def calcDistances(self, points):
        import math
        res = []
        for x, y in points: res.append([math.sqrt(x**2 + y**2), x, y])
        return res

    def randomize(self, points):
        import random
        for i in range(len(points) - 1, 0, -1):
            r = int(random.random() * i)
            points[i], points[r] = points[r], points[i]
        return points

    def partition(self, points, start, end):
        pv = points[start][0]
        points[start], points[end] = points[end], points[start]
        p = start
        for i in range(start, end):
            if points[i][0] < pv:
                points[p], points[i] = points[i], points[p]
                p += 1
        points[p], points[end] = points[end], points[p]
        return p

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K >= len(points): return points
        pd = self.randomize(self.calcDistances(points))
        l, r = 0, len(points) - 1
        p = self.partition(pd, l, r)
        while p != K:
            if p < K: l = p + 1
            else: r = p - 1
            p = self.partition(pd, l, r)

        res = []
        for i, p in enumerate(pd):
            if i == K: break
            res.append(p[1:])
        return res

t = Solution()


print("[[0,2],[-3,3],[-2,5]] =|= ", t.kClosest([[6,10],[-3,3],[-2,5],[0,2]], 3))
print("[[-2,2]] =|= ", t.kClosest([[1,3],[-2,2]], 1))
print("[[3,3],[-2,4]] =|= ", t.kClosest([[3,3],[5,-1],[-2,4]], 2))
print("[[3,3],[5,-1],[-2,4]] =|= ", t.kClosest([[3,3],[5,-1],[-2,4]], 3))