# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an
# array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

from typing import List
from utils import checkValue


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def check(s):
            for c in strs:
                if not c.startswith(s):
                    return False
            return True

        l, r = -1, max(len(s) for s in strs) + 1
        while r - l > 1:
            mid = l + (r - l) // 2
            if check(strs[0][:mid]):
                l = mid
            else:
                r = mid
        return strs[0][:l]


s = Solution()
checkValue("fl", s.longestCommonPrefix(["flower", "flow", "flight"]))
checkValue("a", s.longestCommonPrefix(["ab", "a"]))
