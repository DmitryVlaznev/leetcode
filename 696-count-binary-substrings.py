# 696. Count Binary Substrings

# Easy

# Give a string s, count the number of non-empty (contiguous) substrings
# that have the same number of 0's and 1's, and all the 0's and all the
# 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times
# they occur.

# Example 1:
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of
# consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

# Notice that some of these substrings repeat and are counted the number
# of times they occur.

# Also, "00110011" is not a valid substring because all the 0's (and
# 1's) are not grouped together.

# Example 2:
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have
# equal number of consecutive 1's and 0's.

# Note:
# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.

from utils import checkValue


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0

        if s[0] == "0":
            zo, cur = [1, 0], "0"
        else:
            zo, cur = [0, 1], "1"

        for l in s[1:]:
            if l == cur:
                zo[int(cur)] += 1
            else:
                res += min(zo[0], zo[1])
                cur = l
                zo[int(cur)] = 1
        res += min(zo[0], zo[1])
        return res


t = Solution()

checkValue(6, t.countBinarySubstrings("00110011"))
checkValue(4, t.countBinarySubstrings("10101"))
checkValue(1, t.countBinarySubstrings("10"))
checkValue(1, t.countBinarySubstrings("01"))
checkValue(0, t.countBinarySubstrings("0000"))
checkValue(0, t.countBinarySubstrings("0"))