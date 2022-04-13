# 59. Spiral Matrix II

# Medium

# Given a positive integer n, generate an n x n matrix filled with
# elements from 1 to n2 in spiral order.

# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# Constraints:
# 1 <= n <= 20

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[None] * n for _ in range(n)]
        x, y, i, d = 0, 0, 1, 0
        while i <= n ** 2:
            res[x][y] = i
            xn, yn = x + dirs[d][0], y + dirs[d][1]
            if 0 <= xn < n and 0 <= yn < n and res[xn][yn] is None:
                x, y = xn, yn
            else:
                d = d + 1 if d < 3 else 0
                x, y = x + dirs[d][0], y + dirs[d][1]
            i += 1
        return res

    def generateMatrix2(self, n: int) -> List[List[int]]:
        res = [[None] * n for r in range(n)]

        r, c, d, p, target = 0, 0, "right", 1, n ** 2
        while p <= target:
            res[r][c] = p
            p += 1

            if d == "right":
                if c < n - 1 and res[r][c + 1] is None:
                    c += 1
                else:
                    r += 1
                    d = "down"
            elif d == "down":
                if r < n - 1 and res[r + 1][c] is None:
                    r += 1
                else:
                    c -= 1
                    d = "left"
            elif d == "left":
                if c > 0 and res[r][c - 1] is None:
                    c -= 1
                else:
                    r -= 1
                    d = "up"
            elif d == "up":
                if r > 0 and res[r - 1][c] is None:
                    r -= 1
                else:
                    c += 1
                    d = "right"
        return res


t = Solution()
print(t.generateMatrix(2))
print(t.generateMatrix(3))
print(t.generateMatrix(4))