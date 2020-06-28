# 1044. Longest Duplicate Substring

# Given a string S, consider all duplicated substrings: (contiguous)
# substrings of S that occur 2 or more times.  (The occurrences may
# overlap.)

# Return any duplicated substring that has the longest possible length.
# (If S does not have a duplicated substring, the answer is "".)

# Example 1:
# Input: "banana"
# Output: "ana"

# Example 2:
# Input: "abcd"
# Output: ""

# Note:
# 2 <= S.length <= 10^5
# S consists of lowercase English letters.

from typing import List


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        a = 26
        mod = 2**32

        l, r = 1, n
        while l <= r:
            ll = l + (r - l) // 2
            if self.find(ll, a, mod, n, nums) != -1: l = ll + 1
            else: r = ll - 1
        start = self.find(l - 1, a, mod, n, nums)
        return S[start: start + l - 1]

    def find(self, ll: int, a: int, mod: int, n: int, nums: List[int]) -> str:
        h = 0
        for i in range(ll): h = (h * a + nums[i]) % mod
        seen = {h}
        aL = pow(a, ll, mod)
        for start in range(1, n - ll + 1):
            h = (h * a - nums[start - 1] * aL + nums[start + ll - 1]) % mod
            if h in seen: return start
            seen.add(h)
        return -1

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log("ana", t.longestDupSubstring("banana"))
log("", t.longestDupSubstring("abcd"))