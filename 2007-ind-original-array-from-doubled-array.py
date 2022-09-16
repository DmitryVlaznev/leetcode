# 2007. Find Original Array From Doubled Array

# Medium

# An integer array original is transformed into a doubled array changed
# by appending twice the value of every element in original, and then
# randomly shuffling the resulting array.

# Given an array changed, return original if changed is a doubled array.
# If changed is not a doubled array, return an empty array. The elements
# in original may be returned in any order.


# Example 1:
# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].

# Example 2:
# Input: changed = [6,3,0,1]
# Output: []
# Explanation: changed is not a doubled array.

# Example 3:
# Input: changed = [1]
# Output: []
# Explanation: changed is not a doubled array.

# Constraints:
# 1 <= changed.length <= 10^5
# 0 <= changed[i] <= 10^5

from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if not changed or len(changed) % 2 == 1:
            return []
        changed.sort()
        res = []
        l = r = len(changed) - 1
        while len(res) < len(changed) / 2 and l >= 0 and r >= 0:
            if changed[r] == None:
                r -= 1
                l = min(l, r)
                continue
            if changed[l] == None or changed[l] != changed[r] / 2:
                l -= 1
                continue
            res.append(changed[l])
            changed[l] = changed[r] = None
        return res if len(res) == len(changed) / 2 else []


s = Solution()
# s.findOriginalArray([1, 3, 4, 2, 6, 8])
s.findOriginalArray([6, 3, 0, 1])
