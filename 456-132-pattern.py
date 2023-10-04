# 456. 132 Pattern

# Given an array of n integers nums, a 132 pattern is a subsequence of
# three integers nums[i], nums[j] and nums[k] such that i < j < k and
# nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return
# false.

# Follow up: The O(n^2) is trivial, could you come up with the O(n logn)
# or the O(n) solution?

# Example 1:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.

# Example 2:
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

# Example 3:
# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

# Constraints:
# n == nums.length
# 1 <= n <= 104
# -109 <= nums[i] <= 109

from typing import List
from utils import checkValue


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        l = len(nums)
        if l < 3:
            return False
        mins = [None] * l
        mins[0] = nums[0]
        for i, n in enumerate(nums[1:]):
            mins[i + 1] = min(mins[i], n)

        k = l
        for i in range(l - 1, -1, -1):
            if nums[i] > mins[i]:
                while k < l and nums[k] <= mins[i]:
                    k += 1
                if k < l and nums[k] < nums[i]:
                    return True
                k -= 1
                nums[k] = nums[i]
        return False

    def find132pattern2(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        l_mins = [nums[0]]
        for i in range(1, len(nums)):
            l_mins.append(min(l_mins[i - 1], nums[i]))

        import heapq

        h = []
        for i in range(len(nums) - 1, 0, -1):
            while h and h[0] <= l_mins[i]:
                heapq.heappop(h)
            if h and nums[i] > h[0]:
                return True
            if nums[i] > l_mins[i]:
                heapq.heappush(h, nums[i])
        return False


t = Solution()

checkValue(False, t.find132pattern([1, 2, 3, 4]))
checkValue(True, t.find132pattern([3, 1, 4, 2]))
checkValue(True, t.find132pattern([-1, 3, 2, 0]))
