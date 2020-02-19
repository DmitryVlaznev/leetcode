# 442. Find All Duplicates in an Array

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]

from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set()
        for num in nums:
            i = abs(num) - 1
            if nums[i] < 0:
                res.add(i + 1)
                continue
            nums[i] = -1 * nums[i]
        return list(res)

test = Solution()
print("[2, 3] = ", test.findDuplicates([4,3,2,7,8,2,3,1]))
print("[] = ", test.findDuplicates([1,3,2]))
print("[1] = ", test.findDuplicates([1,1,1]))