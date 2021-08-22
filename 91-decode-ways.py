# Decode Ways

# Medium

# A message containing letters from A-Z is being encoded to numbers
# using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26

# Given a non-empty string containing only digits, determine the total
# number of ways to decode it.

# The answer is guaranteed to fit in a 32-bit integer.

# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: s = "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF"
# (2 2 6).

# Example 3:
# Input: s = "0"
# Output: 0

# Explanation: There is no character that is mapped to a number starting
# with '0'. We cannot ignore a zero when we face it while decoding. So,
# each '0' should be part of "10" --> 'J' or "20" --> 'T'.

# Example 4:
# Input: s = "1"
# Output: 1


# Constraints:
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

from utils import checkValue
from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        letters = {str(i): chr(ord("A") + i - 1) for i in range(1, 27)}

        @lru_cache(maxsize=None)
        def dfs(s: str, start):
            if start == len(s):
                return 1

            res = 0
            if s[start : start + 1] in letters:
                res += dfs(s, start + 1)
            if start + 2 <= len(s) and s[start : start + 2] in letters:
                res += dfs(s, start + 2)
            return res

        res = dfs(s, 0)
        return res if res is not None else 0


class Solution2:
    def __init__(self):
        self.memo = {}

    def recursive_with_memo(self, index, s) -> int:
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == "0":
            return 0

        if index == len(s) - 1:
            return 1

        # Memoization is needed since we might encounter the same sub-string.
        if index in self.memo:
            return self.memo[index]

        ans = self.recursive_with_memo(index + 1, s) + (
            self.recursive_with_memo(index + 2, s)
            if (int(s[index : index + 2]) <= 26)
            else 0
        )

        # Save for memoization
        self.memo[index] = ans

        return ans

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.recursive_with_memo(0, s)


t = Solution()
checkValue(2, t.numDecodings("12"))
checkValue(3, t.numDecodings("226"))
checkValue(0, t.numDecodings("0"))
checkValue(1, t.numDecodings("102"))
checkValue(1, t.numDecodings("10"))
checkValue(0, t.numDecodings("00002"))
checkValue(1, t.numDecodings("2101"))
checkValue(0, t.numDecodings("021"))
checkValue(3, t.numDecodings("1201234"))
checkValue(0, t.numDecodings("111111111111111111111111111111111111111111111"))
