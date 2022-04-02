# 249. Group Shifted Strings

# Medium

# We can shift a string by shifting each of its letters to its
# successive letter.

# For example, "abc" can be shifted to be "bcd".
# We can keep shifting the string to form a sequence.

# For example, we can keep shifting "abc" to form the sequence: "abc" ->
# "bcd" -> ... -> "xyz".
# Given an array of strings strings, group all strings[i] that belong to
# the same shifting sequence. You may return the answer in any order.

# Example 1:
# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

# Example 2:
# Input: strings = ["a"]
# Output: [["a"]]


# Constraints:
# 1 <= strings.length <= 200
# 1 <= strings[i].length <= 50
# strings[i] consists of lowercase English letters.

from typing import List
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        t = ord("z") - ord("a")
        for s in strings:
            h = []
            for i in range(len(s) - 1):
                d = ord(s[i + 1]) - ord(s[i])
                if d < 0:
                    d = t + d + 1
                h.append(str(d))
            res["|".join(h)].append(s)
        return res.values()


s = Solution()
print(s.groupStrings(["az", "ba"]))
print(s.groupStrings(["az", "yx"]))
