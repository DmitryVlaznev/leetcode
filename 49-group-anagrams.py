# 49.Group Anagrams

# Given an array of strings, group anagrams together.

# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for item in strs:
            key = ''.join(sorted(item))
            if key in groups:
                groups[key].append(item)
            else:
                groups[key] = [item]

        res = []
        for key in groups:
            res.append(groups[key])

        return res

t = Solution()
print(t.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))