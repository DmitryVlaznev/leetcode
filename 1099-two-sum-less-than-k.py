# 1099. Two Sum Less Than K

# Given an array A of integers and integer K, return the maximum S such
# that there exists i < j with A[i] + A[j] = S and S < K. If no i, j
# exist satisfying this equation, return -1.

# Example 1:
# Input: A = [34,23,1,24,75,33,54,8], K = 60
# Output: 58
# Explanation: We can use 34 and 24 to sum 58 which is less than 60.

# Example 2:
# Input: A = [10,20,30], K = 15
# Output: -1
# Explanation: In this case it is not possible to get a pair sum less that 15.

# Constraints:
# 1 <= A.length <= 100
# 1 <= A[i] <= 1000
# 1 <= K <= 2000

from typing import List
from utils import checkValue


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return -1

        nums.sort()
        res = -1
        for i in range(len(nums)):
            l, r = i, len(nums)
            while r - l > 1:
                mid = l + (r - l) // 2
                if nums[i] + nums[mid] < k:
                    l = mid
                else:
                    r = mid

            if l > i:
                res = max(res, nums[i] + nums[l])
        return res

    def twoSumLessThanK2(self, A: List[int], K: int) -> int:
        if len(A) < 2:
            return -1

        import bisect

        A.sort()

        res = -1
        for i, n in enumerate(A[1:]):
            candidates = bisect.bisect_left(A, K - n, 0, i + 1)
            if candidates > 0:
                res = max(res, n + A[candidates - 1])
        return res


t = Solution()

checkValue(58, t.twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60))
# checkValue(-1, t.twoSumLessThanK([10, 20, 30], 15))
# checkValue(-1, t.twoSumLessThanK([34], 60))
# checkValue(-1, t.twoSumLessThanK([], 60))
# checkValue(50, t.twoSumLessThanK([10, 20, 30], 60))

# checkValue(
#     1794,
#     t.twoSumLessThanK(
#         [
#             358,
#             898,
#             450,
#             732,
#             672,
#             672,
#             256,
#             542,
#             320,
#             573,
#             423,
#             543,
#             591,
#             280,
#             399,
#             923,
#             920,
#             254,
#             135,
#             952,
#             115,
#             536,
#             143,
#             896,
#             411,
#             722,
#             815,
#             635,
#             353,
#             486,
#             127,
#             146,
#             974,
#             495,
#             229,
#             21,
#             733,
#             918,
#             314,
#             670,
#             671,
#             537,
#             533,
#             716,
#             140,
#             599,
#             758,
#             777,
#             185,
#             549,
#         ],
#         1800,
#     ),
# )
