# 1010. Pairs of Songs With Total Durations Divisible by 60

# Medium

# You are given a list of songs where the ith song has a duration of
# time[i] seconds.

# Return the number of pairs of songs for which their total duration in
# seconds is divisible by 60. Formally, we want the number of indices i,
# j such that i < j with (time[i] + time[j]) % 60 == 0.

# Example 1:
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60

# Example 2:
# Input: time = [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is
# divisible by 60.

# Constraints:
# 1 <= time.length <= 6 * 104
# 1 <= time[i] <= 500

from typing import List
from utils import checkValue


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if len(time) < 2:
            return 0
        remainders = {}
        res = 0
        for song in time:
            r = song % 60
            if r == 0 and 60 in remainders:
                res += remainders[60]
            elif r in remainders:
                res += remainders[r]

            if 60 - r in remainders:
                remainders[60 - r] += 1
            else:
                remainders[60 - r] = 1
        return res


t = Solution()
checkValue(3, t.numPairsDivisibleBy60([30, 20, 150, 100, 40]))
checkValue(3, t.numPairsDivisibleBy60([60, 60, 60]))
checkValue(2, t.numPairsDivisibleBy60([60, 20, 60, 40]))
checkValue(0, t.numPairsDivisibleBy60([60]))
checkValue(0, t.numPairsDivisibleBy60([120]))
checkValue(0, t.numPairsDivisibleBy60([12]))
checkValue(0, t.numPairsDivisibleBy60([12, 43, 57]))
