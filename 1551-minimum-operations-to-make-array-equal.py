# 1551. Minimum Operations to Make Array Equal

# Medium

# You have an array arr of length n where arr[i] = (2 * i) + 1 for all
# valid values of i (i.e. 0 <= i < n).

# In one operation, you can select two indices x and y where 0 <= x, y <
# n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x]
# -=1 and arr[y] += 1). The goal is to make all the elements of the
# array equal. It is guaranteed that all the elements of the array can
# be made equal using some operations.

# Given an integer n, the length of the array. Return the minimum number
# of operations needed to make all the elements of arr equal.

# Example 1:
# Input: n = 3
# Output: 2
# Explanation: arr = [1, 3, 5]
# First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
# In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

# Example 2:
# Input: n = 6
# Output: 9

# Constraints:
# 1 <= n <= 10^4

from utils import checkValue


class Solution:
    def minOperations(self, n: int) -> int:
        mid, odd = n // 2, n % 2
        t = 2 * mid + odd
        l = mid - 2 + odd
        return l * (t - l - 2) + t - odd


t = Solution()
checkValue(0, t.minOperations(1))
checkValue(1, t.minOperations(2))
checkValue(2, t.minOperations(3))
checkValue(4, t.minOperations(4))
checkValue(6, t.minOperations(5))
checkValue(9, t.minOperations(6))
checkValue(12, t.minOperations(7))
checkValue(16, t.minOperations(8))
