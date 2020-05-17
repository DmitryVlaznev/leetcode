# 438. Find All Anagrams in a String

# Given a string s and a non-empty string p, find all the start indices
# of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of
# both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

from typing import List


class Solution:

    def isAnagram(self, wd, pd, keys):
        if set(wd.keys()) != keys: return False
        return len([k for k in keys if wd[k] != pd[k]]) == 0

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not len(s) or not len(p): return []

        p_keys_set = set()
        p_hash = {}
        for k in p:
            p_keys_set.add(k)
            if k not in p_hash: p_hash[k] = 0
            p_hash[k] += 1

        pl = len(p)
        ptr = 0
        window = {}
        res = []
        while ptr < len(s):
            if s[ptr] not in window: window[s[ptr]] = 0
            window[s[ptr]] += 1

            if ptr >= pl:
                window[s[ptr - pl]] -= 1
                if window[s[ptr - pl]] == 0: del window[s[ptr - pl]]

            if ptr >= pl - 1 and self.isAnagram(window, p_hash, p_keys_set):
                res.append(ptr - pl + 1)
            ptr += 1
        return res


def log(correct, res):
    if set(correct) == set(res): print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log([0, 6], t.findAnagrams("cbaebabacd", "abc"))
log([0, 1, 2], t.findAnagrams("abab", "ab"))
log([], t.findAnagrams("abab", "re"))
log([], t.findAnagrams("abab", ""))
log([], t.findAnagrams("", "sdf"))
log([], t.findAnagrams("asd", "sdfsdfsfds"))
log([], t.findAnagrams("asdwsddss", "234"))