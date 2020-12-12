# 163. Missing Ranges

# Easy

# You are given an inclusive range [lower, upper] and a sorted unique
# integer array nums, where all elements are in the inclusive range.

# A number x is considered missing if x is in the range [lower, upper]
# and x is not in nums.

# Return the smallest sorted list of ranges that cover every missing
# number exactly. That is, no element of nums is in any of the ranges,
# and each missing number is in one of the ranges.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b


# Example 1:
# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: ["2","4->49","51->74","76->99"]
# Explanation: The ranges are:
# [2,2] --> "2"
# [4,49] --> "4->49"
# [51,74] --> "51->74"
# [76,99] --> "76->99"

# Example 2:
# Input: nums = [], lower = 1, upper = 1
# Output: ["1"]
# Explanation: The only missing range is [1,1], which becomes "1".

# Example 3:
# Input: nums = [], lower = -3, upper = -1
# Output: ["-3->-1"]
# Explanation: The only missing range is [-3,-1], which becomes
# "-3->-1".

# Example 4:
# Input: nums = [-1], lower = -1, upper = -1
# Output: []
# Explanation: There are no missing ranges since there are no missing
# numbers.

# Example 5:
# Input: nums = [-1], lower = -2, upper = -1
# Output: ["-2"]

# Constraints:
# -109 <= lower <= upper <= 109
# 0 <= nums.length <= 100
# lower <= nums[i] <= upper
# All the values of nums are unique.

from typing import List
from utils import checkList


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res, start, fmt = (
            [],
            lower,
            lambda a, b: str(a) if a == b else str(a) + "->" + str(b),
        )
        for n in nums:
            if start < n:
                res.append(fmt(start, n - 1))
            start = n + 1
        if start <= upper:
            res.append(fmt(start, upper))
        return res


t = Solution()
checkList(
    ["2", "4->49", "51->74", "76->99"], t.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
)
checkList(["1"], t.findMissingRanges([], 1, 1))
checkList(["-3->-1"], t.findMissingRanges([], -3, -1))
checkList([], t.findMissingRanges([-1], -1, -1))
checkList(["-2"], t.findMissingRanges([-1], -2, -1))
checkList([], t.findMissingRanges([1, 2, 3], 1, 3))
checkList(["4"], t.findMissingRanges([1, 2, 3], 1, 4))
checkList(["0"], t.findMissingRanges([1, 2, 3], 0, 3))
checkList(["-1->0"], t.findMissingRanges([1, 2, 3], -1, 3))
checkList(["4->5"], t.findMissingRanges([1, 2, 3], 1, 5))