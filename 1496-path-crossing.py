# 1496. Path Crossing

# Easy

# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each
# representing moving one unit north, south, east, or west,
# respectively. You start at the origin (0, 0) on a 2D plane and walk on
# the path specified by path.

# Return true if the path crosses itself at any point, that is, if at
# any time you are on a location you have previously visited. Return
# false otherwise.


# Example 1:
# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than
# once.

# Example 2:
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.


# Constraints:

# 1 <= path.length <= 10^4
# path[i] is either 'N', 'S', 'E', or 'W'.


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited, point = set(), [0, 0]
        visited.add((0, 0))
        d = {"N": (1, 0), "S": (-1, 0), "E": (0, 1), "W": (0, -1)}
        for l in path:
            point = [point[0] + d[l][0], point[1] + d[l][1]]
            if tuple(point) in visited:
                return True
            visited.add(tuple(point))
        return False


s = Solution()
s.isPathCrossing("NESWW")
