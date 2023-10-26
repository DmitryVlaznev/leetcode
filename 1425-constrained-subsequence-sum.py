# 1425. Constrained Subsequence Sum

# Hard

# Given an integer array nums and an integer k, return the maximum sum
# of a non-empty subsequence of that array such that for every two
# consecutive integers in the subsequence, nums[i] and nums[j], where i
# < j, the condition j - i <= k is satisfied.

# A subsequence of an array is obtained by deleting some number of
# elements (can be zero) from the array, leaving the remaining elements
# in their original order.

# Example 1:
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subsequence is [10, 2, 5, 20].

# Example 2:
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subsequence must be non-empty, so we choose the largest number.

# Example 3:
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subsequence is [10, -2, -5, 20].


# Constraints:
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

from typing import List
from functools import lru_cache


class Solution:
    # O(n)
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        from collections import deque

        dq = deque()
        res = float("-inf")
        for i in range(len(nums)):
            while dq and i - dq[0][1] > k:
                dq.popleft()
            l = dq[0][0] + nums[i] if dq else nums[i]
            res = max(res, l)
            while dq and dq[-1][0] < l:
                dq.pop()
            if l > 0:
                dq.append((l, i))
        return res

    # O(n log n)
    def constrainedSubsetSum2(self, nums: List[int], k: int) -> int:
        import heapq

        h = [(-nums[0], 0)]
        res = nums[0]
        for i in range(1, len(nums)):
            while i - h[0][1] > k:
                heapq.heappop(h)

            curr = max(0, -h[0][0]) + nums[i]
            res = max(res, curr)
            heapq.heappush(h, (-curr, i))

        return res

    # TLE
    def constrainedSubsetSum3(self, nums: List[int], k: int) -> int:
        @lru_cache(maxsize=None)
        def dp(start_index):
            nonlocal k
            tail = nums[start_index]
            max_delta = min(k + 1, len(nums) - start_index - 1)
            for j in range(1, max_delta):
                tail = max(tail, nums[start_index] + dp(start_index + j))
            return tail

        res = max(nums)
        for i in range(len(nums)):
            res = max(res, dp(i))
        return res


s = Solution()
s.constrainedSubsetSum([10, 2, -10, 5, 20], 2)
