# 367. Valid Perfect Square

# Given a positive integer num, write a function which returns True if
# num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while r - l > 1:
            mid = l + (r - l) // 2
            if mid ** 2 < num: l = mid
            else: r = mid
        return r ** 2 == num

t = Solution()
print("True = ", t.isPerfectSquare(16))
print("True = ", t.isPerfectSquare(1))
print("True = ", t.isPerfectSquare(100))
print("False = ", t.isPerfectSquare(2))
print("False = ", t.isPerfectSquare(14))