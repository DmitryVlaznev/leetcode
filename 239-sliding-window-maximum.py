# 239. Sliding Window Maximum

# Hard

# You are given an array of integers nums, there is a sliding window of
# size k which is moving from the very left of the array to the very
# right. You can only see the k numbers in the window. Each time the
# sliding window moves right by one position.

# Return the max sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Example 3:
# Input: nums = [1,-1], k = 1
# Output: [1,-1]

# Example 4:
# Input: nums = [9,11], k = 2
# Output: [11]

# Example 5:
# Input: nums = [4,-2], k = 2
# Output: [4]

# Constraints:
# * 1 <= nums.length <= 105
# * -104 <= nums[i] <= 104
# * 1 <= k <= nums.length

from typing import List
from utils import checkList


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        if k < 2:
            return nums

        from collections import deque

        dq = deque()
        p = 0

        while p < min(len(nums), k):
            while dq and nums[p] >= nums[dq[-1]]:
                dq.pop()
            dq.append(p)
            p += 1

        res, p = [], k
        while p < len(nums):
            res.append(nums[dq[0]])

            while dq and dq[0] <= p - k:
                dq.popleft()

            while dq and nums[p] >= nums[dq[-1]]:
                dq.pop()
            dq.append(p)
            p += 1

        res.append(nums[dq[0]])
        return res


t = Solution()

checkList([3, 3, 5, 5, 6, 7], t.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
checkList([1], t.maxSlidingWindow([1], 1))
checkList([1], t.maxSlidingWindow([1], 2))
checkList([3], t.maxSlidingWindow([1, 3], 24))
checkList([1, -1], t.maxSlidingWindow([1, -1], 1))
checkList([1], t.maxSlidingWindow([1, -1], 2))
checkList([11], t.maxSlidingWindow([9, 11], 2))
checkList([7, 4], t.maxSlidingWindow([7, 2, 4], 2))
