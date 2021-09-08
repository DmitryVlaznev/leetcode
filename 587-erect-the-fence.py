# 587. Erect the Fence

# Hard

# You are given an array trees where trees[i] = [xi, yi] represents the
# location of a tree in the garden.

# You are asked to fence the entire garden using the minimum length of
# rope as it is expensive. The garden is well fenced only if all the
# trees are enclosed.

# Return the coordinates of trees that are exactly located on the fence
# perimeter.

# Example 1:
# Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

# Example 2:
# Input: points = [[1,2],[2,2],[4,2]]
# Output: [[4,2],[2,2],[1,2]]

# Constraints:
# 1 <= points.length <= 3000
# points[i].length == 2
# 0 <= xi, yi <= 100
# All the given points are unique.

from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p1, p2, p3):
            return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

        if len(trees) < 3:
            return trees
        points = [(x, y) for x, y in trees]
        points.sort()

        lower = []
        for p in points:
            while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # When all points reside in a line we need to remove duplicates
        return list(set(lower[:-1] + upper[:-1]))


s = Solution()
s.outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]])
s.outerTrees([[1, 2], [2, 2], [4, 2]])
