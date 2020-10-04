# K-diff Pairs in an Array

# Given an array of integers nums and an integer k, return the number of
# unique k-diff pairs in the array.

# A k-diff pair is an integer pair (nums[i], nums[j]), where the
# following are true:
# 0 <= i, j < nums.length
# i != j
# a <= b
# b - a == k


# Example 1:
# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3,
# 5). Although we have two 1s in the input, we should only return the
# number of unique pairs.

# Example 2:
# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3),
# (3, 4) and (4, 5).

# Example 3:
# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).

# Example 4:
# Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
# Output: 2

# Example 5:
# Input: nums = [-1,-2,-3], k = 1
# Output: 2

# Example 6:
# Input: nums = [-3,-2,-1], k = 1
# Output: 2

# Constraints:
# 1 <= nums.length <= 104
# -10^7 <= nums[i] <= 107
# 0 <= k <= 107

from typing import List
import utils

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        processed = {}
        counted = set()
        res = 0

        for n in nums:
            if (n - k) in processed and (n - k, n) not in counted:
                counted.add((n - k,n))
                res += 1
            if (n + k) in processed and (n, n + k) not in counted:
                counted.add((n, n + k))
                res += 1
            processed[n] = True
        return res

t = Solution()
utils.checkValue(2, t.findPairs([3,1,4,1,5], 2))
utils.checkValue(2, t.findPairs([1,1,3,4,5], 2))
utils.checkValue(2, t.findPairs([5,4,3,1,1], 2))
utils.checkValue(4, t.findPairs([1,2,3,4,5], 1))
utils.checkValue(1, t.findPairs([1,3,1,5,4], 0))
utils.checkValue(2, t.findPairs([1,2,4,4,3,3,0,9,2,3], 3))
utils.checkValue(2, t.findPairs([-1,-2,-3], 1))
utils.checkValue(2, t.findPairs([-3,-2,-1], 1))

utils.checkValue(0, t.findPairs([3,1,4,1,5], 5))
utils.checkValue(0, t.findPairs([], 5))
