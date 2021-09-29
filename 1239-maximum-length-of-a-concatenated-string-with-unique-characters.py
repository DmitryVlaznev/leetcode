# 1239. Maximum Length of a Concatenated String with Unique Characters

# Medium

# Given an array of strings arr. String s is a concatenation of a
# sub-sequence of arr which have unique characters.

# Return the maximum possible length of s.

# Example 1:
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All possible concatenations are "","un","iq","ue","uniq"
# and "ique".
# Maximum length is 4.

# Example 2:
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".

# Example 3:
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26

# Constraints:
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lower case English letters.

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def get_mask(s: str):
            res = 0
            for l in s:
                b = 1 << (ord(l) - ord("a"))
                if res & b:
                    return None
                res |= b
            return res

        words, masks = [], {}
        for i in range(len(arr)):
            m = get_mask(arr[i])
            if m is not None:
                words.append(arr[i])
                masks[arr[i]] = m

        res = 0

        def dfs(cur_mask, cur_len, i):
            nonlocal res

            if i == len(words):
                return

            # without i-th word
            res = max(res, cur_len)
            dfs(cur_mask, cur_len, i + 1)

            # with i-th word
            if not cur_mask & masks[words[i]]:
                cur_len += len(words[i])
                cur_mask |= masks[words[i]]
                res = max(res, cur_len)
                dfs(cur_mask, cur_len, i + 1)

        dfs(0, 0, 0)
        return res
