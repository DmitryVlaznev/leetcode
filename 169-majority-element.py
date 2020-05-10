# Majority Element

# Given an array of size n, find the majority element. The majority
# element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = None
        counter = 0
        for n in nums:
            if counter == 0:
                cur = n
                counter = 1
                continue
            if n == cur: counter += 1
            else: counter -= 1
        return cur
        # threshold = len(nums) // 2
        # counts = {}
        # for n in nums:
        #     if n not in counts: counts[n] = 1
        #     else: counts[n] = counts[n] + 1
        #     if counts[n] > threshold: return n

t = Solution()
print("3 = ", t.majorityElement([3,2,3]))
print("2 = ", t.majorityElement([2,2,1,1,1,2,2]))
print("42 = ", t.majorityElement([42]))