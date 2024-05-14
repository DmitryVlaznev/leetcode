# 514. Freedom Trail

# Hard

# In the video game Fallout 4, the quest "Road to Freedom" requires
# players to reach a metal dial called the "Freedom Trail Ring" and use
# the dial to spell a specific keyword to open the door.

# Given a string ring that represents the code engraved on the outer
# ring and another string key that represents the keyword that needs to
# be spelled, return the minimum number of steps to spell all the
# characters in the keyword.

# Initially, the first character of the ring is aligned at the "12:00"
# direction. You should spell all the characters in key one by one by
# rotating ring clockwise or anticlockwise to make each character of the
# string key aligned at the "12:00" direction and then by pressing the
# center button.

# At the stage of rotating the ring to spell the key character key[i]:

# You can rotate the ring clockwise or anticlockwise by one place, which
# counts as one step. The final purpose of the rotation is to align one
# of ring's characters at the "12:00" direction, where this character
# must equal key[i]. If the character key[i] has been aligned at the
# "12:00" direction, press the center button to spell, which also counts
# as one step. After the pressing, you could begin to spell the next
# character in the key (next stage). Otherwise, you have finished all
# the spelling.


# Example 1:
# Input: ring = "godding", key = "gd"
# Output: 4
# Explanation:
# For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
# For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
# Also, we need 1 more step for spelling.
# So the final output is 4.

# Example 2:
# Input: ring = "godding", key = "godding"
# Output: 13


# Constraints:

# 1 <= ring.length, key.length <= 100
# ring and key consist of only lower case English letters.
# It is guaranteed that key could always be spelled by rotating ring.

from functools import cache


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        @cache
        def dp(ring_i, key_i):
            if key_i == len(key):
                return 0
            if ring[ring_i] == key[key_i]:
                return 1 + dp(ring_i, key_i + 1)

            # check left direction
            steps, i = 0, ring_i
            while ring[i] != key[key_i]:
                i = i - 1 if i - 1 >= 0 else len(ring) - 1
                steps += 1
            left_res = 1 + steps + dp(i, key_i + 1)

            # check right direction
            steps, i = 0, ring_i
            while ring[i] != key[key_i]:
                i = i + 1 if i + 1 < len(ring) else 0
                steps += 1
            right_res = 1 + steps + dp(i, key_i + 1)

            return min(left_res, right_res)

        return dp(0, 0)


s = Solution()
s.findRotateSteps("godding", "gd")
