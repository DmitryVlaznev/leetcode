# 1392. Longest Happy Prefix

# A string is called a happy prefix if is a non-empty prefix which is
# also a suffix (excluding itself).

# Given a string s. Return the longest happy prefix of s .

# Return an empty string if no such prefix exists.

# Example 1:
# Input: s = "level"
# Output: "l"
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev",
# "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix
# which is also suffix is given by "l".


# Example 2:
# Input: s = "ababab"
# Output: "abab"
# Explanation: "abab" is the largest prefix which is also suffix. They
# can overlap in the original string.

# Example 3:
# Input: s = "leetcodeleet"
# Output: "leet"

# Example 4:
# Input: s = "a"
# Output: ""

# Constraints:
# 1 <= s.length <= 10^5
# s contains only lowercase English letters.

class Solution:
    def longestPrefix(self, s: str) -> str:
        pf = [0] * len(s)
        for i in range(1, len(s)):
            j = pf[i - 1]
            while j > 0 and s[i] != s[j]: j = pf[j - 1]
            if s[i] == s[j]: j+=1
            pf[i] = j
        return s[:pf[-1]]

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log("l", t.longestPrefix("level"))
log("abab", t.longestPrefix("ababab"))
log("leet", t.longestPrefix("leetcodeleet"))
log("", t.longestPrefix("a"))