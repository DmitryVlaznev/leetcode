# 994. Rotting Oranges

# Medium

# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.

# Every minute, any fresh orange that is adjacent (4-directionally) to a
# rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell
# has a fresh orange.  If this is impossible, return -1 instead.

# Example 1:
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1

# Explanation:  The orange in the bottom left corner (row 2, column 0)
# is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: [[0,2]]
# Output: 0

# Explanation:  Since there are already no fresh oranges at minute 0,
# the answer is just 0.

# Note:
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.

from typing import List
from utils import checkValue


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        rows, cols = len(grid), len(grid[0])

        fresh = 0
        dq = deque()
        days_passed = 0

        for r in range(rows):
            for c in range(cols):
                fresh = fresh + 1 if grid[r][c] == 1 else fresh
                if grid[r][c] == 2:
                    dq.append((r, c))

        while fresh and dq:
            days_passed += 1
            l = len(dq)
            while l:
                l -= 1
                r, c = dq.popleft()
                if r > 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    fresh -= 1
                    dq.append((r - 1, c))
                if r < rows - 1 and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    fresh -= 1
                    dq.append((r + 1, c))
                if c > 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    fresh -= 1
                    dq.append((r, c - 1))
                if c < cols - 1 and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    fresh -= 1
                    dq.append((r, c + 1))

        return days_passed if fresh == 0 else -1


t = Solution()

checkValue(4, t.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
checkValue(-1, t.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
checkValue(0, t.orangesRotting([[0, 2]]))
