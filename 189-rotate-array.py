# 189. Rotate Array

# Given an array, rotate the array to the right by k steps, where k is
# non-negative.

# Follow up:

# Try to come up as many solutions as you can, there are at least 3
# different ways to solve this problem.

# Could you do it in-place with O(1) extra space?


# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


# Constraints:
# 1 <= nums.length <= 2 * 104
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

from typing import List
from utils import checkList

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, p, q):
            while p < q:
                arr[p], arr[q] = arr[q], arr[p]
                p += 1
                q -= 1

        l = len(nums)
        if l < 2: return nums

        k = k % l
        if k == 0: return
        reverse(nums, 0, l - k - 1)
        reverse(nums, l - k, l - 1)

        p, q, n = 0, l - 1, k
        while n:
            nums[p], nums[q] = nums[q], nums[p]
            p += 1
            q -= 1
            n -= 1
        if k < l - k - 1:
            reverse(nums, k, l - k - 1)
        elif l - k < k - 1:
            reverse(nums, l - k, k - 1)

t = Solution()

arr = [1,2,3,4,5,6,7]
t.rotate(arr, 3)
checkList([5,6,7,1,2,3,4], arr)

arr = [1,2,3,4,5,6,7]
t.rotate(arr, 2)
checkList([6,7,1,2,3,4,5], arr)

arr = [1,2,3,4,5,6,7]
t.rotate(arr, 1)
checkList([7,1,2,3,4,5,6], arr)

arr = [1,2,3,4,5,6,7]
t.rotate(arr, 5)
checkList([3,4,5,6,7,1,2], arr)

arr = [1,2,3,4,5,6,7,8]
t.rotate(arr, 4)
checkList([5,6,7,8,1,2,3,4], arr)

arr = [1,2]
t.rotate(arr, 5)
checkList([2,1], arr)

arr = [1]
t.rotate(arr, 5)
checkList([1], arr)

arr = []
t.rotate(arr, 5)
checkList([], arr)