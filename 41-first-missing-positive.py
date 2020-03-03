# 41. First Missing Positive

# Given an unsorted integer array, find the smallest missing positive
# integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1
# Note:

# Your algorithm should run in O(n) time and uses constant extra space.

from typing import List


class Solution:
    def collectAllPositivesAtTheEnd(self, nums: List[int]) -> int:
        '''
        Collect all positive numbers at the end of the list.
        We will treat 0 as non-positive.
        Spend O(n) time and O(1) space.

        Return an index when a non-negative sequence starts.
        '''
        l = len(nums)
        n = l - 1
        p = 0
        while p <= n and n >=0 and p < l:
            if nums[n] <= 0 and nums[p] > 0:
                nums [p], nums[n] = nums[n], nums[p]
            if nums[n] > 0:
                n -= 1
            if nums[p] <= 0:
                p += 1
        return p

    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 1
        positivesStartAt = self.collectAllPositivesAtTheEnd(nums)
        # All numbers are negative
        if positivesStartAt == l:
            return 1

        # Turn all negatives to positives, since we will use an array as
        # a hash
        for i in range(0, positivesStartAt):
            if nums[i] == 0:
                nums[i] = 1
            else:
                nums[i] *= -1

        i = positivesStartAt
        while i < l:
            index = abs(nums[i]) - 1
            i += 1
            if index >= 0 and index < l and nums[index] > 0:
                nums[index] *= -1

        missed = 0
        while missed < l and nums[missed] < 0:
            missed += 1

        return missed + 1

test = Solution()

print("1 = ", test.firstMissingPositive([3,4,0,2]))
print("4 = ", test.firstMissingPositive([1,0,3,3,0,2]))
print("1 = ", test.firstMissingPositive([2, 2]))
print("3 = ", test.firstMissingPositive([1, 2, 0]))
print("2 = ", test.firstMissingPositive([3, 4, -1, 1]))
print("4 = ", test.firstMissingPositive([3, 2, -1, 1]))
print("5 = ", test.firstMissingPositive([3, -5, 4, 2, 1, -12]))
print("5 = ", test.firstMissingPositive([3, -5, 4, 2, 1, -14, -42]))
print("1 = ", test.firstMissingPositive([7, 8, 9, 11, 12]))
print("1 = ", test.firstMissingPositive([-7, -8, -9, -11, -12]))
print("1 = ", test.firstMissingPositive([-7, -8, -9, 11, 12]))
print("1 = ", test.firstMissingPositive([7, 8, 9, -11, -12]))
print("1 = ", test.firstMissingPositive([7, -8, 9, -11, -12]))
print("2 = ", test.firstMissingPositive([1, -8, 1, -11, -12]))
print("1 = ", test.firstMissingPositive([0, -8, 0, -11, -12]))
print("2 = ", test.firstMissingPositive([0, -8, 0, 1, 0]))
print("1 = ", test.firstMissingPositive([0, 0, 0]))
print("2 = ", test.firstMissingPositive([1, 1]))
print("2 = ", test.firstMissingPositive([1, -11]))
print("3 = ", test.firstMissingPositive([1, 1, 2, 1, 2, 2, -11]))
print("3 = ", test.firstMissingPositive([1, 1, 2, 1, 2, 2]))
