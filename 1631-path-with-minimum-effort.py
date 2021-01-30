# 1631. Path With Minimum Effort

# Medium

# You are a hiker preparing for an upcoming hike. You are given heights,
# a 2D array of size rows x columns, where heights[row][col] represents
# the height of cell (row, col). You are situated in the top-left cell,
# (0, 0), and you hope to travel to the bottom-right cell, (rows-1,
# columns-1) (i.e., 0-indexed). You can move up, down, left, or right,
# and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between
# two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to
# the bottom-right cell.

# Example 1:
# Input: heights = [
#   [1,2,2],
#   [3,8,2],
#   [5,3,5]
# ]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute
# difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum
# absolute difference is 3.

# Example 2:
# Input: heights = [
#   [1,2,3],
#   [3,8,4],
#   [5,3,5]
# ]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute
# difference of 1 in consecutive cells, which is better than route
# [1,3,5,3,5].

# Example 3:
# Input: heights = [
#   [1,2,1,1,1],
#   [1,2,1,2,1],
#   [1,2,1,2,1],
#   [1,2,1,2,1],
#   [1,1,1,2,1]
# ]
# Output: 0
# Explanation: This route does not require any effort.

# Constraints:
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 10^6

from typing import List
from utils import checkValue


class Solution:
    def checkEffort(self, heights: List[List[int]], maxEffort) -> bool:
        rows, cols = len(heights), len(heights[0])
        visited = [[False] * cols for _ in range(rows)]
        from collections import deque

        dq = deque()
        visited[0][0] = True
        dq.append((0, 0, 0))
        paths = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while dq:
            l = len(dq)
            while l:
                r, c, d = dq.popleft()
                if r == rows - 1 and c == cols - 1:
                    return True
                for dx, dy in paths:
                    nr, nc = r + dx, c + dy

                    if nr < 0 or nr > rows - 1 or nc < 0 or nc > cols - 1:
                        continue
                    if visited[nr][nc]:
                        continue
                    effort = abs(heights[r][c] - heights[nr][nc])
                    if effort > maxEffort:
                        continue

                    visited[nr][nc] = True
                    dq.append((nr, nc, max(d, effort)))
                l -= 1
        return False

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        l, r = -1, 10 ** 6
        while r - l > 1:
            mid = l + (r - l) // 2
            if self.checkEffort(heights, mid):
                r = mid
            else:
                l = mid
        return r


t = Solution()

heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
checkValue(2, t.minimumEffortPath(heights))

heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
checkValue(1, t.minimumEffortPath(heights))

heights = [
    [1, 2, 1, 1, 1],
    [1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1],
    [1, 1, 1, 2, 1],
]
checkValue(0, t.minimumEffortPath(heights))

checkValue(0, t.minimumEffortPath([[4]]))