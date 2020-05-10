# 1232. Check If It Is a Straight Line

# You are given an array coordinates, coordinates[i] = [x, y], where [x,
# y] represents the coordinate of a point. Check if these points make a
# straight line in the XY plane.

# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

# Constraints:

# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        cc =coordinates
        a = cc[0][1] - cc[1][1]
        b = cc[1][0] - cc[0][0]
        c = cc[0][0] * cc[1][1] - cc[1][0] * cc[0][1]

        for i in range(1, len(cc) -1):
            if a * cc[i][0] + b * cc[i][1] + c != 0: return False
        return True

t = Solution()
print("True", t.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print("False", t.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
print("True", t.checkStraightLine([[1,1],[2,2]]))