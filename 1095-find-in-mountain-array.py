# 1095. Find in Mountain Array

# (This problem is an interactive problem.)

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that
# mountainArr.get(index) == target. If such an index does not exist,
# return -1.

# You cannot access the mountain array directly. You may only access the
# array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k
# (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be
# judged Wrong Answer. Also, any solutions that attempt to circumvent
# the judge will result in disqualification.


# Example 1:
# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the
# minimum index, which is 2.

# Example 2:
# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.


# Constraints:
# 3 <= mountain_arr.length() <= 10^4
# 0 <= target <= 10^9
# 0 <= mountain_arr.get(index) <= 10^9

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, arr):
        self.arr = arr
        self.access = 0

    def get(self, index: int) -> int:
        self.access += 1
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)

    def get_access(self) -> int:
        return self.access


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        if target < min(
            mountain_arr.get(0), mountain_arr.get(mountain_arr.length() - 1)
        ):
            return -1

        l, r = -1, mountain_arr.length()
        while r - l > 1:
            mid = l + (r - l) // 2
            if mountain_arr.get(mid + 1) < mountain_arr.get(mid):
                r = mid
            else:
                l = mid

        max_index = r
        if target > mountain_arr.get(max_index):
            return -1

        l, r = -1, max_index
        while r - l > 1:
            mid = l + (r - l) // 2
            if mountain_arr.get(mid) <= target:
                l = mid
            else:
                r = mid
        if l >= 0 and mountain_arr.get(l) == target:
            return l

        l, r = max_index - 1, mountain_arr.length()
        while r - l > 1:
            mid = l + (r - l) // 2
            if mountain_arr.get(mid) >= target:
                l = mid
            else:
                r = mid
        if l < mountain_arr.length() and mountain_arr.get(l) == target:
            return l

        return -1


from utils import checkValue


m = MountainArray([3, 5, 3, 2, 0])
s = Solution()
checkValue(4, s.findInMountainArray(0, m))
print("access = ", m.get_access())

m = MountainArray([3, 5, 3, 2, 0])
s = Solution()
checkValue(-1, s.findInMountainArray(1, m))
print("access = ", m.get_access())