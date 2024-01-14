# 1980. Find Unique Binary String

# Medium

# Given an array of strings nums containing n unique binary strings each
# of length n, return a binary string of length n that does not appear
# in nums. If there are multiple answers, you may return any of them.

# Example 1:
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.

# Example 2:
# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.

# Example 3:
# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and
# "110" would also be correct.

# Constraints:
# n == nums.length
# 1 <= n <= 16
# nums[i].length == n
# nums[i] is either '0' or '1'.
# All the strings of nums are unique.

from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        inums = set()
        for s in nums:
            inums.add(int(s, 2))
        for i in range(2**16):
            if i not in inums:
                res = "{0:b}".format(i)
                if len(res) < len(nums):
                    prefix = "".join((["0"] * (len(nums) - len(res))))
                    res = prefix + res
                return res
