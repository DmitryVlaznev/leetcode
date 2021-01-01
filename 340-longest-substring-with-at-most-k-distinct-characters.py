# 340. Longest Substring with At Most K Distinct Characters

# Medium

# Given a string s and an integer k, return the length of the longest
# substring of s that contains at most k distinct characters.

# Example 1:
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.

# Example 2:
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.

# Constraints:
# 1 <= s.length <= 5 * 104
# 0 <= k <= 50

from utils import checkValue


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        p, q, seen, l = 0, 0, {}, 0
        while p < len(s):
            if s[p] not in seen:
                seen[s[p]] = 0
            seen[s[p]] += 1
            if len(seen) <= k:
                l = max(l, p - q + 1)
            while len(seen) > k:
                seen[s[q]] -= 1
                if seen[s[q]] == 0:
                    seen.pop(s[q])
                q += 1
            p += 1
        return l


t = Solution()
checkValue(3, t.lengthOfLongestSubstringKDistinct("eceba", 2))
checkValue(0, t.lengthOfLongestSubstringKDistinct("eceba", 0))
checkValue(1, t.lengthOfLongestSubstringKDistinct("eceba", 1))
checkValue(3, t.lengthOfLongestSubstringKDistinct("ecebbba", 1))
checkValue(2, t.lengthOfLongestSubstringKDistinct("aa", 1))
checkValue(0, t.lengthOfLongestSubstringKDistinct("", 13))