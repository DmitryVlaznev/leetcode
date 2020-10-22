# 735. Asteroid Collision

# We are given an array asteroids of integers representing asteroids in
# a row.

# For each asteroid, the absolute value represents its size, and the
# sign represents its direction (positive meaning right, negative
# meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two
# asteroids meet, the smaller one will explode. If both are the same
# size, both will explode. Two asteroids moving in the same direction
# will never meet.

# Example 1:
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10.  The 5 and 10
# never collide.

# Example 2:
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.

# Example 3:
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5
# collide resulting in 10.

# Example 4:

# Input: asteroids = [-2,-1,1,2]
# Output: [-2,-1,1,2]
# Explanation: The -2 and -1 are moving left, while the 1 and 2 are
# moving right. Asteroids moving the same direction never meet, so no
# asteroids will meet each other.

# Constraints:
# 1 <= asteroids <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0

from typing import List
from utils import checkList


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return asteroids

        stack = []
        stack.append(asteroids[0])
        p = 1
        while p < len(asteroids):
            if stack and stack[-1] > 0 and asteroids[p] < 0:
                # collision
                right = asteroids[p]
                while stack and stack[-1] > 0 and right < 0:
                    left = stack.pop()

                    if abs(left) == abs(right):
                        right = 0
                    elif abs(left) > abs(right):
                        right = 0
                        stack.append(left)
                if right != 0:
                    stack.append(right)
            else:
                stack.append(asteroids[p])
            p += 1

        return stack


t = Solution()

checkList([5, 10], t.asteroidCollision([5, 10, -5]))
checkList([], t.asteroidCollision([8, -8]))
checkList([10], t.asteroidCollision([10, 2, -5]))
checkList([-2, -1, 1, 2], t.asteroidCollision([-2, -1, 1, 2]))
checkList([-2], t.asteroidCollision([-2]))
checkList([2], t.asteroidCollision([2]))
checkList([], t.asteroidCollision([]))
