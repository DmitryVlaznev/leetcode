# 395. Longest Substring with At Least K Repeating Characters

# Medium

# Given a string s and an integer k, return the length of the longest
# substring of s such that the frequency of each character in this
# substring is more than or equal to k.

# Example 1:
# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3
# times.

# Example 2:
# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2
# times and 'b' is repeated 3 times.

# Constraints:
# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 105

from utils import checkValue


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        from collections import Counter

        counts, p = Counter(s), 0
        while p < len(s):
            if counts[s[p]] < k:
                return max(
                    self.longestSubstring(s[0:p], k),
                    self.longestSubstring(s[p + 1 : len(s)], k),
                )
            p += 1
        return len(s)


t = Solution()
checkValue(5, t.longestSubstring("ababbc", 2))
checkValue(3, t.longestSubstring("aaabb", 3))
checkValue(6, t.longestSubstring("baaabb", 3))
checkValue(0, t.longestSubstring("bacvb", 3))
checkValue(10, t.longestSubstring("bacvbrrrrr", 1))
checkValue(0, t.longestSubstring("w", 3))
checkValue(3, t.longestSubstring("bbaaacbd", 3))
checkValue(0, t.longestSubstring("ababacb", 3))
checkValue(0, t.longestSubstring("aabcabb", 3))
