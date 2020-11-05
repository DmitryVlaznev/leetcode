# 1146. Consecutive Characters

# Given a string s, the power of the string is the maximum length of a
# non-empty substring that contains only one unique character.

# Return the power of the string.


# Example 1:
# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e'
# only.

# Example 2:
# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character
# 'e' only.

# Example 3:
# Input: s = "triplepillooooow"
# Output: 5

# Example 4:
# Input: s = "hooraaaaaaaaaaay"
# Output: 11

# Example 5:
# Input: s = "tourist"
# Output: 1


# Constraints:
# 1 <= s.length <= 500
# s contains only lowercase English letters.

from utils import checkValue


class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        max_len, cur_len, last_letter = 1, 1, s[0]
        for letter in s[1:]:
            if letter == last_letter:
                cur_len += 1
                max_len = max(cur_len, max_len)
            else:
                cur_len, last_letter = 1, letter
        return max_len


t = Solution()

checkValue(2, t.maxPower("leetcode"))
checkValue(5, t.maxPower("abbcccddddeeeeedcba"))
checkValue(5, t.maxPower("triplepillooooow"))
checkValue(11, t.maxPower("hooraaaaaaaaaaay"))
checkValue(1, t.maxPower("tourist"))
checkValue(2, t.maxPower("qqtourist"))
checkValue(2, t.maxPower("touristqq"))
checkValue(2, t.maxPower("qq"))
checkValue(1, t.maxPower("q"))
checkValue(0, t.maxPower(""))
