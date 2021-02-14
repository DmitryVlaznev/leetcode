# 1091. Shortest Path in Binary Matrix

# Medium

# In an N by N square grid, each cell is either empty (0) or blocked
# (1).

# A clear path from top-left to bottom-right has length k if and only if
# it is composed of cells C_1, C_2, ..., C_k such that:

# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie.,
# they are different and share an edge or corner)

# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c]
# == 0).
# Return the length of the shortest such clear path from top-left to
# bottom-right.  If such a path does not exist, return -1.

# Example 1:
# Input: [[0,1],[1,0]]
# Output: 2

# Example 2:
# Input: [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Note:
# 1 <= grid.length == grid[0].length <= 100
# grid[r][c] is 0 or 1

from typing import List
from utils import checkValue
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        seen = [[False] * n for _ in range(n)]
        d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        dq = deque()
        res = 1
        dq.append((0, 0))
        seen[0][0] = True
        while dq:
            l = len(dq)
            while l:
                l -= 1
                r, c = dq.popleft()
                if r == c == n - 1:
                    return res
                for dr, dc in d:
                    rn, cn = r + dr, c + dc
                    if (
                        rn < 0
                        or rn >= n
                        or cn < 0
                        or cn >= n
                        or grid[rn][cn]
                        or seen[rn][cn]
                    ):
                        continue
                    dq.append((rn, cn))
                    seen[rn][cn] = True
            res += 1
        return -1


t = Solution()

checkValue(2, t.shortestPathBinaryMatrix([[0, 1], [1, 0]]))
checkValue(4, t.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
checkValue(-1, t.shortestPathBinaryMatrix([[1, 1], [1, 0]]))
checkValue(-1, t.shortestPathBinaryMatrix([[0, 0, 0], [0, 1, 1], [0, 1, 0]]))
