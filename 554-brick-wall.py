# 554. Brick Wall

# Medium

# There is a brick wall in front of you. The wall is rectangular and has
# several rows of bricks. The bricks have the same height but different
# width. You want to draw a vertical line from the top to the bottom and
# cross the least bricks.

# The brick wall is represented by a list of rows. Each row is a list of
# integers representing the width of each brick in this row from left to
# right.

# If your line go through the edge of a brick, then the brick is not
# considered as crossed. You need to find out how to draw the line to
# cross the least bricks and return the number of crossed bricks.

# You cannot draw a line just along one of the two vertical edges of the
# wall, in which case the line will obviously cross no bricks.


# Example:
# Input: [[1,2,2,1],
#         [3,1,2],
#         [1,3,2],
#         [2,4],
#         [3,1,2],
#         [1,3,1,1]]

# Output: 2

# Note:
# * The width sum of bricks in different rows are the same and won't
#   exceed INT_MAX.
# * The number of bricks in each row is in range [1,10,000]. The height
#   of wall is in range [1,10,000]. Total number of bricks of the wall
#   won't exceed 20,000.

from typing import List
from utils import checkValue


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall or not wall[0]:
            return 0
        edges = {}
        for row in wall:
            s = 0
            for brick in row[0:-1]:
                s += brick
                if s not in edges:
                    edges[s] = 0
                edges[s] += 1
        e = [n for _, n in edges.items()]
        return len(wall) - max(e or [0])


t = Solution()

wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
checkValue(2, t.leastBricks(wall))

wall = [[1, 2, 2, 1]]
checkValue(0, t.leastBricks(wall))

wall = [[1, 2], [3]]
checkValue(1, t.leastBricks(wall))

wall = [[3], [3]]
checkValue(2, t.leastBricks(wall))

wall = [[3, 1], [1, 3]]
checkValue(1, t.leastBricks(wall))

wall = [[]]
checkValue(0, t.leastBricks(wall))
