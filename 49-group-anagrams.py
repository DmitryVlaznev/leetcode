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
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for item in strs:
            groups["".join(sorted(item))].append(item)
        return groups.values()


t = Solution()
print(t.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))