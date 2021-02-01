# Squirrel Simulation

# Medium

# There's a tree, a squirrel, and several nuts. Positions are
# represented by the cells in a 2D grid. Your goal is to find the
# minimal distance for the squirrel to collect all the nuts and put them
# under the tree one by one. The squirrel can only take at most one nut
# at one time and can move in four directions - up, down, left and
# right, to the adjacent cell. The distance is represented by the number
# of moves.

# Example 1:
# Input:
# Height : 5
# Width : 7
# Tree position : [2,2]
# Squirrel : [4,4]
# Nuts : [[3,0], [2,5]]
# Output: 12


# Note:
# * All given positions won't overlap.
# * The squirrel can take at most one nut at one time.
# * The given positions of nuts have no order.
# * Height and width are positive integers. 3 <= height * width <= 10,000.
# * The given positions contain at least one nut, only one tree and one squirrel.

from typing import List
from utils import checkValue


class Solution:
    def minDistance(
        self,
        height: int,
        width: int,
        tree: List[int],
        squirrel: List[int],
        nuts: List[List[int]],
    ) -> int:
        diff, res = float("-inf"), None
        for i, j in nuts:
            tnt_dist = 2 * (abs(tree[0] - i) + abs(tree[1] - j))
            snt_dist = (
                abs(tree[0] - i)
                + abs(tree[1] - j)
                + abs(squirrel[0] - i)
                + abs(squirrel[1] - j)
            )
            cur_diff = tnt_dist - snt_dist
            if cur_diff > diff:
                res = res + diff if res is not None else 0
                res += snt_dist
                diff = cur_diff
            else:
                res += tnt_dist
        return res


t = Solution()

checkValue(12, t.minDistance(5, 7, [2, 2], [4, 4], [[3, 0], [2, 5]]))
checkValue(11, t.minDistance(5, 3, [0, 0], [0, 3], [[0, 2], [0, 5]]))
