# 283. Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        nz = z = 0
        while z < l and nums[z] != 0:
            z +=1
        nz = z + 1
        while nz < l and z < l:
            if nums[z] == 0 and nums[nz] != 0: nums[z], nums[nz] = nums[nz], nums[z]
            if nums[z] != 0: z += 1
            if nums[nz] == 0: nz += 1

t = Solution()

arr = [0,1,0,3,12]
t.moveZeroes(arr)
print(arr)

arr = [1,0,2,0,3,12]
t.moveZeroes(arr)
print(arr)

arr = [0,0,0,1,2,3]
t.moveZeroes(arr)
print(arr)

arr = [0,0,0,1,2,3,0,0,0]
t.moveZeroes(arr)
print(arr)

arr = [1,2,3,0,0,0,4,5,6]
t.moveZeroes(arr)
print(arr)

arr = [1,0,2,0,3,12,0]
t.moveZeroes(arr)
print(arr)

arr = [1,3,12]
t.moveZeroes(arr)
print(arr)

arr = [0,0,0]
t.moveZeroes(arr)
print(arr)

arr = []
t.moveZeroes(arr)
print(arr)

arr = [1]
t.moveZeroes(arr)
print(arr)

arr = [0]
t.moveZeroes(arr)
print(arr)
