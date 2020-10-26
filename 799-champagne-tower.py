# 799. Champagne Tower

# We stack glasses in a pyramid, where the first row has 1 glass, the
# second row has 2 glasses, and so on until the 100th row.  Each glass
# holds one cup (250ml) of champagne.

# Then, some champagne is poured in the first glass at the top.  When
# the topmost glass is full, any excess liquid poured will fall equally
# to the glass immediately to the left and right of it.  When those
# glasses become full, any excess champagne will fall equally to the
# left and right of those glasses, and so on.  (A glass at the bottom
# row has its excess champagne fall on the floor.)

# For example, after one cup of champagne is poured, the top most glass
# is full.  After two cups of champagne are poured, the two glasses on
# the second row are half full.  After three cups of champagne are
# poured, those two cups become full - there are 3 full glasses total
# now.  After four cups of champagne are poured, the third row has the
# middle glass half full, and the two outside glasses are a quarter
# full, as pictured below.

# Now after pouring some non-negative integer cups of champagne, return
# how full the jth glass in the ith row is (both i and j are 0-indexed.)

# Example 1:
# Input: poured = 1, query_row = 1, query_glass = 1
# Output: 0.00000
# Explanation: We poured 1 cup of champagne to the top glass of the
# tower (which is indexed as (0, 0)). There will be no excess liquid so
# all the glasses under the top glass will remain empty.

# Example 2:
# Input: poured = 2, query_row = 1, query_glass = 1
# Output: 0.50000
# Explanation: We poured 2 cups of champagne to the top glass of the
# tower (which is indexed as (0, 0)). There is one cup of excess liquid.
# The glass indexed as (1, 0) and the glass indexed as (1, 1) will share
# the excess liquid equally, and each will get half cup of champagne.

# Example 3:
# Input: poured = 100000009, query_row = 33, query_glass = 17
# Output: 1.00000


# Constraints:
# 0 <= poured <= 109
# 0 <= query_glass <= query_row < 100

from utils import checkValue

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0 for x in range(query_row + 1)] for y in range(query_row + 1)]
        glasses[0][0] = poured
        for r in range(1, query_row + 1):
            for c in range(0, query_row + 1):
                if c == 0:
                    glasses[r][c] = 0 if glasses[r - 1][c] <= 1 else (glasses[r - 1][c] - 1) * 0.5
                elif c == r:
                    glasses[r][c] = 0 if glasses[r - 1][c - 1] <= 1 else (glasses[r - 1][c - 1] - 1) * 0.5
                else:
                    from_left = (glasses[r - 1][c - 1] - 1) * 0.5 if glasses[r - 1][c - 1] > 1 else 0
                    from_right = (glasses[r - 1][c] - 1) * 0.5 if glasses[r - 1][c] > 1 else 0
                    glasses[r][c] = from_left + from_right
        return 1 if glasses[query_row][query_glass] > 1 else glasses[query_row][query_glass]

t = Solution()
checkValue(1, t.champagneTower(100000009, 33, 17))
checkValue(0, t.champagneTower(1, 1, 1))
checkValue(0.5, t.champagneTower(2, 1, 1))
checkValue(1, t.champagneTower(1, 0, 0))

