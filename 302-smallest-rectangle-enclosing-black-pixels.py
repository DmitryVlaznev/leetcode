# 302. Smallest Rectangle Enclosing Black Pixels

# Hard

# You are given an m x n binary matrix image where 0 represents a white
# pixel and 1 represents a black pixel.

# The black pixels are connected (i.e., there is only one black region).
# Pixels are connected horizontally and vertically.

# Given two integers x and y that represents the location of one of the
# black pixels, return the area of the smallest (axis-aligned) rectangle
# that encloses all black pixels.

# You must write an algorithm with less than O(mn) runtime complexity

# Example 1:
# Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
# Output: 6

# Example 2:
# Input: image = [["1"]], x = 0, y = 0
# Output: 1

# Constraints:
# m == image.length
# n == image[i].length
# 1 <= m, n <= 100
# image[i][j] is either '0' or '1'.
# 1 <= x < m
# 1 <= y < n
# image[x][y] == '1'.
# The black pixels in the image only form one component.

from typing import List
from utils import checkValue


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        t, r, b, l = y, x, y, x

        def canGo(x, y):
            if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
                return False
            return image[x][y] == "1"

        def dfs(x, y):
            nonlocal t, r, b, l
            d = [[0, -1], [1, 0], [0, 1], [-1, 0]]

            image[x][y] = "#"
            t, r, b, l = min(t, y), max(r, x), max(b, y), min(l, x)
            for dx, dy in d:
                if canGo(x + dx, y + dy):
                    dfs(x + dx, y + dy)

        dfs(x, y)
        return (b - t + 1) * (r - l + 1)


s = Solution()

checkValue(
    6,
    s.minArea([["0", "0", "1", "0"], ["0", "1", "1", "0"], ["0", "1", "0", "0"]], 0, 2),
)
checkValue(1, s.minArea([["1"]], 0, 0))
