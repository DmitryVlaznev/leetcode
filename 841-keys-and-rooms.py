# 841. Keys and Rooms

# Medium

# There are N rooms and you start in room 0.  Each room has a distinct
# number in 0, 1, 2, ..., N-1, and each room may have some keys to
# access the next room.

# Formally, each room i has a list of keys rooms[i], and each key
# rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.
# A key rooms[i][j] = v opens the room with number v.

# Initially, all the rooms start locked (except for room 0).

# You can walk back and forth between rooms freely.

# Return true if and only if you can enter every room.

# Example 1:
# Input: [[1],[2],[3],[]]
# Output: true
# Explanation:
# We start in room 0, and pick up key 1.
# We then go to room 1, and pick up key 2.
# We then go to room 2, and pick up key 3.
# We then go to room 3.  Since we were able to go to every room, we
# return true.

# Example 2:
# Input: [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can't enter the room with number 2.
# Note:

# 1 <= rooms.length <= 1000
# 0 <= rooms[i].length <= 1000
# The number of keys in all rooms combined is at most 3000.

from typing import List
from utils import checkValue
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        not_visited = set([i for i in range(1, len(rooms))])
        dq = deque()
        dq.append(0)
        while dq:
            l = len(dq)
            while l:
                l -= 1
                room = dq.popleft()
                keys = rooms[room]
                for key in keys:
                    if key in not_visited:
                        not_visited.remove(key)
                        dq.append(key)
        return len(not_visited) == 0


t = Solution()
checkValue(True, t.canVisitAllRooms([[1], [2], [3], []]))
checkValue(True, t.canVisitAllRooms([[0]]))
checkValue(True, t.canVisitAllRooms([[]]))
checkValue(False, t.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
