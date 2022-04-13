# 763. Partition Labels

# Medium

# A string S of lowercase English letters is given. We want to partition
# this string into as many parts as possible so that each letter appears
# in at most one part, and return a list of integers representing the
# size of these parts.

# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because
# it splits S into less parts.


# Note:
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.

from typing import List
from utils import checkList


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_letters = {c: i for i, c in enumerate(S)}

        res, cur_start, cur_end = [], 0, 0
        for i, c in enumerate(S):
            cur_end = max(cur_end, last_letters[c])
            if i == cur_end:
                res.append(cur_end - cur_start + 1)
                cur_start = i + 1
        return res


t = Solution()

checkList([9, 7, 8], t.partitionLabels("ababcbacadefegdehijhklij"))
checkList([7], t.partitionLabels("defegde"))