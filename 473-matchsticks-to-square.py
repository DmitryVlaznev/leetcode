# 473. Matchsticks to Square

# Medium

# You are given an integer array matchsticks where matchsticks[i] is the
# length of the ith matchstick. You want to use all the matchsticks to
# make one square. You should not break any stick, but you can link them
# up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.


# Example 1:
# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the
# square came two sticks with length 1.


# Example 2:
# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the
# matchsticks.

# Constraints:
# 1 <= matchsticks.length <= 15
# 1 <= matchsticks[i] <= 10^8

from typing import List
from functools import lru_cache


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks = list(reversed(sorted(matchsticks)))
        if len(matchsticks) < 4:
            return False
        p = sum(matchsticks)
        if p % 4:
            return False
        side = p // 4

        @lru_cache(maxsize=None)
        def dp(buckets, i):
            nonlocal side
            if i == len(matchsticks):
                return buckets[0] == buckets[1] == buckets[2] == buckets[3]
            buckets = list(buckets)
            for b in range(4):
                if buckets[b] + matchsticks[i] <= side:
                    buckets[b] += matchsticks[i]
                    if dp(tuple(buckets), i + 1):
                        return True
                    buckets[b] -= matchsticks[i]
            return False

        return dp((0, 0, 0, 0), 0)


s = Solution()
s.makesquare([10, 6, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2])
