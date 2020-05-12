# 540. Single Element in a Sorted Array

# You are given a sorted array consisting of only integers where every
# element appears exactly twice, except for one element which appears
# exactly once. Find this single element that appears only once.

# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10

# Note: Your solution should run in O(log n) time and O(1) space.

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n_len = len(nums)
        l = -1
        r = n_len // 2 + 1
        while r - l > 1:
            mid = l + (r - l) // 2
            if mid * 2 + 1 < n_len and nums[mid * 2] == nums[mid * 2 + 1]: l = mid
            else: r = mid
        return nums[r * 2]

t = Solution()

print("2 = ", t.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print("1 = ", t.singleNonDuplicate([1,2,2,3,3,4,4,8,8]))
print("8 = ", t.singleNonDuplicate([1,1,2,2,3,3,4,4,8]))
print("10 = ", t.singleNonDuplicate([3,3,7,7,10,11,11]))
print("6 = ", t.singleNonDuplicate([1,1,3,3,4,4,5,5,6,8,8]))
print("1 = ", t.singleNonDuplicate([1]))
print("1 = ", t.singleNonDuplicate([1, 2, 2]))
print("2 = ", t.singleNonDuplicate([1, 1, 2]))