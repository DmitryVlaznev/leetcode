# 505. The Maze II

# Medium

# There is a ball in a maze with empty spaces (represented as 0) and
# walls (represented as 1). The ball can go through the empty spaces by
# rolling up, down, left or right, but it won't stop rolling until
# hitting a wall. When the ball stops, it could choose the next
# direction.

# Given the m x n maze, the ball's start position and the destination,
# where start = [startrow, startcol] and destination = [destinationrow,
# destinationcol], return the shortest distance for the ball to stop at
# the destination. If the ball cannot stop at destination, return -1.

# The distance is the number of empty spaces traveled by the ball from
# the start position (excluded) to the destination (included).

# You may assume that the borders of the maze are all walls (see
# examples).

# Example 1:
# Input: maze = [
# [0,0,1,0,0],
# [0,0,0,0,0],
# [0,0,0,1,0],
# [1,1,0,1,1],
# [0,0,0,0,0]], start = [0,4], destination = [4,4]
# Output: 12
# Explanation: One possible way is : left -> down -> left -> down ->
# right -> down -> right.
# The length of the path is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

# Example 2:
# Input: maze = [
# [0,0,1,0,0],
# [0,0,0,0,0],
# [0,0,0,1,0],
# [1,1,0,1,1],
# [0,0,0,0,0]], start = [0,4], destination = [3,2]
# Output: -1
# Explanation: There is no way for the ball to stop at the destination.
# Notice that you can pass through the destination but you cannot stop
# there.

# Example 3:
# Input: maze = [
# [0,0,0,0,0],
# [1,1,0,0,1],
# [0,0,0,0,0],
# [0,1,0,0,1],
# [0,1,0,0,0]], start = [4,3], destination = [0,1]
# Output: -1

# Constraints:
# m == maze.length
# n == maze[i].length
# 1 <= m, n <= 100
# maze[i][j] is 0 or 1.
# start.length == 2
# destination.length == 2
# 0 <= startrow, destinationrow <= m
# 0 <= startcol, destinationcol <= n
# Both the ball and the destination exist in an empty space, and they
# will not be in the same position initially.
# The maze contains at least 2 empty spaces.

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def shortestDistance(self, maze, start, destination):
        m, n, q, stopped = (
            len(maze),
            len(maze[0]),
            [(0, start[0], start[1])],
            {(start[0], start[1]): 0},
        )
        while q:
            dist, x, y = heapq.heappop(q)
            if [x, y] == destination:
                return dist
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                newX, newY, d = x, y, 0
                while (
                    0 <= newX + i < m
                    and 0 <= newY + j < n
                    and maze[newX + i][newY + j] != 1
                ):
                    newX += i
                    newY += j
                    d += 1
                if (newX, newY) not in stopped or dist + d < stopped[(newX, newY)]:
                    stopped[(newX, newY)] = dist + d
                    heapq.heappush(q, (dist + d, newX, newY))
        return -1

    # TLE
    # def shortestDistance(
    #     self, maze: List[List[int]], start: List[int], destination: List[int]
    # ) -> int:
    #     visited = defaultdict(lambda: float("inf"))

    #     def dfs(r, c):
    #         d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    #         for dr, dc in d:
    #             count = 0
    #             rr, cc = r, c
    #             while (
    #                 rr + dr >= 0
    #                 and rr + dr < len(maze)
    #                 and cc + dc >= 0
    #                 and cc + dc < len(maze[0])
    #                 and maze[rr + dr][cc + dc] == 0
    #             ):
    #                 count, rr, cc = count + 1, rr + dr, cc + dc
    #             if visited[(r, c)] + count < visited[(rr, cc)]:
    #                 visited[(rr, cc)] = visited[(r, c)] + count
    #                 dfs(rr, cc)

    #     visited[tuple(start)] = 0
    #     dfs(start[0], start[1])
    #     return (
    #         visited[tuple(destination)]
    #         if visited[tuple(destination)] != float("inf")
    #         else -1
    #     )