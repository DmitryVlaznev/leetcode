# 167. Two Sum II - Input array is sorted

# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that
# they add up to the target, where index1 must be less than index2.

# Note:
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you
# may not use the same element twice.

# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p, q = 0, len(numbers) - 1
        while numbers[p] + numbers[q] != target:
            if numbers[p] + numbers[q] > target: q -= 1
            else: p +=1
        return [p + 1, q + 1]


def log(correct, res):
    if set(correct) == set(res): print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log([1,2], t.twoSum([2,7,11,15], 9))
log([3,6], t.twoSum([1,2,3,7,11,48,51,154,234], 51))