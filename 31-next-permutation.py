# Next Permutation

# Medium

# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the
# lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:
# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:
# Input: nums = [1,1,5]
# Output: [1,5,1]

# Example 4:
# Input: nums = [1]
# Output: [1]

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100


from typing import List
from utils import checkList


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        p, q = len(nums) - 1, -1
        while p > 0 and nums[p - 1] >= nums[p]:
            p -= 1

        if p > 0:
            q = p - 1
            while p < len(nums) - 1 and nums[p + 1] > nums[q]:
                p += 1
            nums[p], nums[q] = nums[q], nums[p]

        l, r = q + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


t = Solution()

nums = [1, 3, 2]
t.nextPermutation(nums)
checkList([2, 1, 3], nums)

nums = [9, 7, 5, 3]
t.nextPermutation(nums)
checkList([3, 5, 7, 9], nums)


nums = [1, 2, 3]
t.nextPermutation(nums)
checkList([1, 3, 2], nums)

nums = [3, 2, 1]
t.nextPermutation(nums)
checkList([1, 2, 3], nums)

nums = [1, 1, 5]
t.nextPermutation(nums)
checkList([1, 5, 1], nums)

nums = [1]
t.nextPermutation(nums)
checkList([1], nums)

nums = [2, 3, 4, 1, 5, 7, 6, 4, 1]
t.nextPermutation(nums)
checkList([2, 3, 4, 1, 6, 1, 4, 5, 7], nums)

nums = [2, 3, 4, 1, 5, 7, 5, 4, 1]
t.nextPermutation(nums)
checkList([2, 3, 4, 1, 7, 1, 4, 5, 5], nums)

nums = [2, 3, 4, 1, 5, 7]
t.nextPermutation(nums)
checkList([2, 3, 4, 1, 7, 5], nums)

nums = [2, 3, 4, 1, 5, 7, 6, 6, 1]
t.nextPermutation(nums)
checkList([2, 3, 4, 1, 6, 1, 5, 6, 7], nums)
