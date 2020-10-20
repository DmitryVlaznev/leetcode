# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without
# repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

from utils import checkValue


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        p, q = 0, 0
        longest_length = 0
        while q < len(s):
            if s[q] in seen:
                while s[p] != s[q]:
                    seen.remove(s[p])
                    p += 1
                p += 1
            else:
                seen.add(s[q])
                longest_length = max(longest_length, q - p + 1)
            q += 1
        return longest_length


t = Solution()

checkValue(3, t.lengthOfLongestSubstring("abcabcbb"))
checkValue(1, t.lengthOfLongestSubstring("bbbbb"))
checkValue(3, t.lengthOfLongestSubstring("pwwkew"))
checkValue(0, t.lengthOfLongestSubstring(""))