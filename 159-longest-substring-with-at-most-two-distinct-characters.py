# 159. Longest Substring with At Most Two Distinct Characters

# Medium

# Given a string s , find the length of the longest substring t  that
# contains at most 2 distinct characters.

# Example 1:
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.

# Example 2:
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.

from utils import checkValue


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        seen = {}
        p, q = 0, 1
        max_len = 1
        seen[s[p]] = 1
        while q < len(s):
            if s[q] in seen:
                seen[s[q]] += 1
            else:
                seen[s[q]] = 1

            if len(seen) < 3:
                max_len = max(q - p + 1, max_len)
            else:
                while len(seen) > 2:
                    seen[s[p]] -= 1
                    if seen[s[p]] == 0:
                        seen.pop(s[p])
                    p += 1
            q += 1
        return max_len


t = Solution()
checkValue(3, t.lengthOfLongestSubstringTwoDistinct("eceba"))
checkValue(5, t.lengthOfLongestSubstringTwoDistinct("ccaabbb"))
checkValue(3, t.lengthOfLongestSubstringTwoDistinct("ccc"))
checkValue(0, t.lengthOfLongestSubstringTwoDistinct(""))
checkValue(1, t.lengthOfLongestSubstringTwoDistinct("f"))