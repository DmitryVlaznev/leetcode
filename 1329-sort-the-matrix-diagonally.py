# 1329. Sort the Matrix Diagonally

# Medium

# A matrix diagonal is a diagonal line of cells starting from some cell
# in either the topmost row or leftmost column and going in the
# bottom-right direction until reaching the matrix's end. For example,
# the matrix diagonal starting from mat[2][0], where mat is a 6 x 3
# matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal in
# ascending order and return the resulting matrix.

# Example 1:
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100

from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        import heapq

        rows, cols = len(mat), len(mat[0])
        r, c = rows - 1, 0
        d = [-1, 0]

        while c < cols:
            hq = []
            ri, ci = r, c
            while ri < rows and ci < cols:
                heapq.heappush(hq, mat[ri][ci])
                ri += 1
                ci += 1
            ri, ci = r, c
            while ri < rows and ci < cols:
                mat[ri][ci] = heapq.heappop(hq)
                ri += 1
                ci += 1
            r += d[0]
            c += d[1]
            if r < 0:
                r, c, d = 0, 1, [0, 1]
        return mat


t = Solution()
print(t.diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))
