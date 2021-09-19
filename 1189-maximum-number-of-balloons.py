# 1189. Maximum Number of Balloons

# Easy

# Given a string text, you want to use the characters of text to form as
# many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum
# number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0

# Constraints:
# 1 <= text.length <= 104
# text consists of lower case English letters only.

from collections import Counter
from utils import checkValue


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        res = float("inf")
        res = min(res, c["b"])
        res = min(res, c["a"])
        res = min(res, c["l"] // 2)
        res = min(res, c["o"] // 2)
        res = min(res, c["n"])
        return res


s = Solution()

checkValue(1, s.maxNumberOfBalloons("nlaebolko"))
checkValue(2, s.maxNumberOfBalloons("loonbalxballpoon"))
checkValue(0, s.maxNumberOfBalloons("leetcode"))
