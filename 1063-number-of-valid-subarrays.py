# 1063. Number of Valid Subarrays

# Given an integer array nums, return the number of non-empty subarrays
# with the leftmost element of the subarray not larger than other
# elements in the subarray.

# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [1,4,2,5,3]
# Output: 11
# Explanation: There are 11 valid subarrays:
# [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].

# Example 2:
# Input: nums = [3,2,1]
# Output: 3
# Explanation: The 3 valid subarrays are: [3],[2],[1].

# Example 3:
# Input: nums = [2,2,2]
# Output: 6
# Explanation: There are 6 valid subarrays:
# [2],[2],[2],[2,2],[2,2],[2,2,2].


# Constraints:
# 1 <= nums.length <= 5 * 10^4
# 0 <= nums[i] <= 10^5

from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack, res = [], 0
        # For every element n we need to find next smaller element k.
        # When we find it the number of arrays will be (ki - ni)
        for r in range(len(nums)):
            while stack and nums[r] < nums[stack[-1]]:
                l = stack.pop()
                res += r - l
            stack.append(r)
        # All elements in the stack do not have a smaller element on the
        # right. So, for each element n in the stack the number of
        # arrays will be len(nums) - ni
        r = len(nums)
        while stack:
            l = stack.pop()
            res += r - l
        return res


s = Solution()
s.validSubarrays([1, 4, 2, 5, 3])
