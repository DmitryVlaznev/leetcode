# 702. Search in a Sorted Array of Unknown Size

# Given an integer array sorted in ascending order, write a function to
# search target in nums.  If target exists, then return its index,
# otherwise return -1. However, the array size is unknown to you. You
# may only access the array using an ArrayReader interface, where
# ArrayReader.get(k) returns the element of the array at index k
# (0-indexed).

# You may assume all integers in the array are less than 10000, and if
# you access the array out of bounds, ArrayReader.get will return
# 2147483647.


# Example 1:
# Input: array = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:
# Input: array = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Constraints:
# You may assume that all elements in the array are unique.
# The value of each element in the array will be in the range [-9999, 9999].
# The length of the array will be in the range [1, 10^4].

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        if index >= len(self.arr):
            return 2147483647
        return self.arr[index]


from utils import checkValue


class Solution:
    def search(self, reader, target):
        l, r = -1, 10 ** 4
        while r - l > 1:
            mid = l + (r - l) // 2
            if reader.get(mid) >= target:
                r = mid
            else:
                l = mid
        return r if reader.get(r) == target else -1


t = Solution()

reader = ArrayReader([-1, 0, 3, 5, 9, 12])
checkValue(4, t.search(reader, 9))

reader = ArrayReader([-1, 0, 3, 5, 9, 12])
checkValue(-1, t.search(reader, 2))

reader = ArrayReader([34])
checkValue(0, t.search(reader, 34))

reader = ArrayReader([43])
checkValue(-1, t.search(reader, 34))