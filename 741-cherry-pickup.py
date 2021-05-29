# 741. Cherry Pickup

# Hard

# You are given an n x n grid representing a field of cherries, each
# cell is one of three possible integers.

# * 0 means the cell is empty, so you can pass through,
# * 1 means the cell contains a cherry that you can pick up and pass
#   through, or
# * -1 means the cell contains a thorn that blocks your way.

# Return the maximum number of cherries you can collect by following the
# rules below:
# * Starting at the position (0, 0) and reaching (n - 1, n - 1) by
#   moving right or down through valid path cells (cells with value 0 or
#   1).
# * After reaching (n - 1, n - 1), returning to (0, 0) by moving left or
#   up through valid path cells.
# * When passing through a path cell containing a cherry, you pick it
#   up, and the cell becomes an empty cell 0.
# * If there is no valid path between (0, 0) and (n - 1, n - 1), then no
#   cherries can be collected.

# Example 1:
# Input: grid = [
#   [ 0, 1,-1],
#   [ 1, 0,-1],
#   [ 1, 1, 1]
# ]
# Output: 5
# Explanation: The player started at (0, 0) and went down, down, right
# right to reach (2, 2). 4 cherries were picked up during this single
# trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]]. Then, the
# player went left, up, up, left to return home, picking up one more
# cherry. The total number of cherries picked up is 5, and this is the
# maximum possible.

# Example 2:
# Input: grid = [
#   [ 1, 1,-1],
#   [ 1,-1, 1],
#   [-1, 1, 1]
# ]
# Output: 0

# Constraints:
# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# grid[i][j] is -1, 0, or 1.
# grid[0][0] != -1
# grid[n - 1][n - 1] != -1

from typing import List
from utils import checkValue


class Solution:
    # Greedy, doesn't work here
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def makePass(grid: List[List[int]]):
            n = len(grid)
            dp = [[None] * (n + 1) for _ in range(n + 1)]
            for r in range(1, n + 1):
                for c in range(1, n + 1):
                    if r == 1 and c == 1:
                        dp[r][c] = [(0, 0)] if grid[0][0] == 1 else []
                        continue
                    if (
                        dp[r - 1][c] is None
                        and dp[r][c - 1] is None
                        or grid[r - 1][c - 1] == -1
                    ):
                        dp[r][c] = None
                        continue
                    u = 0 if dp[r - 1][c] is None else len(dp[r - 1][c])
                    l = 0 if dp[r][c - 1] is None else len(dp[r][c - 1])
                    if u >= l and dp[r - 1][c] is not None:
                        dp[r][c] = dp[r - 1][c][:]
                    else:
                        dp[r][c] = dp[r][c - 1][:]
                    if grid[r - 1][c - 1]:
                        dp[r][c].append((r - 1, c - 1))
            return dp[-1][-1]

        picked = makePass(grid)
        if picked is None:
            return 0
        res = len(picked)
        for r, c in picked:
            grid[r][c] = 0
        grid = list(map(lambda row: row[::-1], grid[::-1]))
        return res + len(makePass(grid))


t = Solution()

grid = [[0, 0, 1], [-1, 0, -1], [-1, 0, 0]]
checkValue(0, t.cherryPickup(grid))

grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
checkValue(5, t.cherryPickup(grid))

grid = [[0, 1, -1], [-1, 0, -1], [1, 1, 1]]
checkValue(3, t.cherryPickup(grid))

grid = [[0, -1, 1], [1, 0, -1], [1, 1, 1]]
checkValue(4, t.cherryPickup(grid))

grid = [[1, 1, -1], [1, -1, 1], [-1, 1, 1]]
checkValue(0, t.cherryPickup(grid))


grid = [
    [1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1],
]
