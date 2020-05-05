# 387. First Unique Character in a String

# Given a string, find the first non-repeating character in it and
# return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

# Note: You may assume the string contain only lowercase letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        encounters = {}
        for i in range(0, len(s)):
            if s[i] in encounters: encounters[s[i]] = None
            else: encounters[s[i]] = i
        idx = float("inf")
        for l in encounters:
            if encounters[l] is not None:
                idx = min(idx, encounters[l])
        return idx if idx != float("inf") else -1
t = Solution()

print("0 = ", t.firstUniqChar("leetcode"))
print("2 = ", t.firstUniqChar("loveleetcode"))
print("-1 = ", t.firstUniqChar("lovelove"))
print("-1 = ", t.firstUniqChar(""))
print("-1 = ", t.firstUniqChar("www"))