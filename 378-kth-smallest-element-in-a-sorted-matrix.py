# 378. Kth Smallest Element in a Sorted Matrix

# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the
# kth distinct element.

# Example:
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
# return 13.

# Example:
# matrix = [
#    [ 1,  2,  13],
#    [ 3,  4,  15],
#    [ 5,  6,  17]
# ],
# k = 8,
# return 15.


# Note:
# You may assume k is always valid, 1 ≤ k ≤ n**2.

from typing import List, Tuple


class Solution:
    def getI(self, matrix: List[List[int]], n: int, i: int) -> int:
        return matrix[(i - 1) // n][(i - 1) % n]

    def setI(self, matrix: List[List[int]], n: int, i: int, v: int):
        matrix[(i - 1) // n][(i - 1) % n] = v

    def sink(self, matrix: List[List[int]], l: int, n: int, i: int):
        while i * 2 <= l:
            ci = i * 2
            if ci + 1 <= l and self.getI(matrix, n, ci + 1) < self.getI(matrix, n, ci):
                ci = ci + 1

            i_v = self.getI(matrix, n, i)
            ci_v = self.getI(matrix, n, ci)

            if i_v < ci_v:
                break
            self.setI(matrix, n, i, ci_v)
            self.setI(matrix, n, ci, i_v)
            i = ci

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l = n ** 2
        p = l // 2
        while p > 0:
            self.sink(matrix, l, n, p)
            p -= 1

        while k > 0:
            m = self.getI(matrix, n, 1)
            tail = self.getI(matrix, n, l)
            self.setI(matrix, n, l, m)
            self.setI(matrix, n, 1, tail)
            l -= 1
            k -= 1
            self.sink(matrix, l, n, 1)

        return self.getI(matrix, n, l + 1)




t = Solution()
matrix = [
   [ 1,  2,  13],
   [ 3,  4,  15],
   [ 5,  6,  17]
]
res = t.kthSmallest(matrix, 8)
print("15 = ", res)

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
res = t.kthSmallest(matrix, 8)
print("13 = ", res)

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
res = t.kthSmallest(matrix, 2)
print("5 = ", res)

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
res = t.kthSmallest(matrix, 9)
print("15 = ", res)

matrix = [
   [ 2,  2],
   [2, 2],
]
res = t.kthSmallest(matrix, 2)
print("2 = ", res)

matrix = [
   [ 42 ],
]
res = t.kthSmallest(matrix, 1)
print("42 = ", res)