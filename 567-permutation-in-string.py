# 567. Permutation in String

# Given two strings s1 and s2, write a function to return true if s2
# contains the permutation of s1. In other words, one of the first
# string's permutations is the substring of the second string.

# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False

# Note:
# * The input strings only contain lower case letters.
# * The length of both given strings is in range [1, 10,000].

from typing import List


class Solution:

    def isPermutation(self, wd, pd, keys):
        if set(wd.keys()) != keys: return False
        return len([k for k in keys if wd[k] != pd[k]]) == 0

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        if not len(s1): return True

        p = s1
        s = s2
        p_keys_set = set()
        p_hash = {}
        for k in p:
            p_keys_set.add(k)
            if k not in p_hash: p_hash[k] = 0
            p_hash[k] += 1

        pl = len(s1)
        ptr = 0
        window = {}
        while ptr < len(s):
            if s[ptr] not in window: window[s[ptr]] = 0
            window[s[ptr]] += 1

            if ptr >= pl:
                window[s[ptr - pl]] -= 1
                if window[s[ptr - pl]] == 0: del window[s[ptr - pl]]

            if ptr >= pl - 1 and self.isPermutation(window, p_hash, p_keys_set):
                return True
            ptr += 1
        return False

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(True, t.checkInclusion("ab", "eidbaooo"))
log(False, t.checkInclusion("ab", "eidboaoo"))

log(True,  t.checkInclusion("abc", "cbaebabacd"))
log(True,  t.checkInclusion("ab", "abab"))
log(False, t.checkInclusion("re", "abab"))
log(False, t.checkInclusion("abab", ""))
log(False, t.checkInclusion("sdf", ""))
log(False, t.checkInclusion("sdfsdfsfds", "asd"))
log(False, t.checkInclusion("234", "asdwsddss"))