# 296. Best Meeting Point

# Hard

# Given an m x n binary grid grid where each 1 marks the home of one
# friend, return the minimal total travel distance.

# The total travel distance is the sum of the distances between the
# houses of the friends and the meeting point.

# The distance is calculated using Manhattan Distance, where
# distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

# Example 1:
# Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# Output: 6
# Explanation: Given three friends living at (0,0), (0,4), and (2,2).
# The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
# So return 6.

# Example 2:
# Input: grid = [[1,1]]
# Output: 1

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# grid[i][j] is either 0 or 1.
# There will be at least two friends in the grid.

from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        def get_horizontal(grid, rows, cols):
            h = []
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c]:
                        h.append(r)
            return h

        def get_vertical(grid, rows, cols):
            v = []
            for c in range(cols):
                for r in range(rows):
                    if grid[r][c]:
                        v.append(c)
            return v

        def get_distance(points):
            distance = 0
            l, r = 0, len(points) - 1
            while l < r:
                distance += points[r] - points[l]
                l, r = l + 1, r - 1
            return distance

        rows, cols = len(grid), len(grid[0])
        h, v = get_horizontal(grid, rows, cols), get_vertical(grid, rows, cols)
        return get_distance(h) + get_distance(v)


s = Solution()
s.minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])
