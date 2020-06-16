# 35. Search Insert Position

# Given a sorted array and a target value, return the index if the
# target is found. If not, return the index where it would be if it were
# inserted in order.

# You may assume no duplicates in the array.

# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6], 2
# Output: 1

# Example 3:
# Input: [1,3,5,6], 7
# Output: 4

# Example 4:
# Input: [1,3,5,6], 0
# Output: 0

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while r - l > 1:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        return r


def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log(2, t.searchInsert([1, 3, 5, 6], 5))
log(1, t.searchInsert([1, 3, 5, 6], 2))
log(4, t.searchInsert([1, 3, 5, 6], 7))
log(0, t.searchInsert([1, 3, 5, 6], 0))
log(0, t.searchInsert([], 42))

