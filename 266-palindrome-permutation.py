# 266. Palindrome Permutation

# Easy

# Given a string, determine if a permutation of the string could form a
# palindrome.

# Example 1:
# Input: "code"
# Output: false

# Example 2:
# Input: "aab"
# Output: true

# Example 3:
# Input: "carerac"
# Output: true

from utils import checkValue


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        memo = {}
        for l in s:
            if l not in memo:
                memo[l] = 0
            memo[l] += 1
        odd = 0
        for _, n in memo.items():
            if n % 2:
                odd += 1
        return odd < 2


t = Solution()

checkValue(False, t.canPermutePalindrome("code"))
checkValue(True, t.canPermutePalindrome("aab"))
checkValue(True, t.canPermutePalindrome("carerac"))
checkValue(True, t.canPermutePalindrome(""))