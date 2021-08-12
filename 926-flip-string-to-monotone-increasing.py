# 926. Flip String to Monotone Increasing

# Medium

# A binary string is monotone increasing if it consists of some number
# of 0's (possibly none), followed by some number of 1's (also possibly
# none).

# You are given a binary string s. You can flip s[i] changing it from 0
# to 1 or from 1 to 0.

# Return the minimum number of flips to make s monotone increasing.


# Example 1:
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.

# Example 2:
# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.

# Example 3:
# Input: s = "00011000"
# Output: 2
# Explanation: We flip to get 00000000.

# Constraints:
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.

from utils import checkValue


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones, zeroes = sum([int(d) for d in s]), 0
        res = min(ones, len(s) - ones)

        for d in reversed(s):
            if d == "1":
                ones -= 1
            else:
                zeroes += 1
            res = min(res, ones + zeroes)
        return res


s = Solution()

checkValue(1, s.minFlipsMonoIncr("00110"))
checkValue(2, s.minFlipsMonoIncr("010110"))
checkValue(0, s.minFlipsMonoIncr("00"))
checkValue(2, s.minFlipsMonoIncr("00011000"))
checkValue(0, s.minFlipsMonoIncr("1"))
checkValue(2, s.minFlipsMonoIncr("10001111011111"))
