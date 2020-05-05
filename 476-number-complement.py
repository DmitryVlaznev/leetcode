# 476. Number Complement

# Given a positive integer, output its complement number. The complement
# strategy is to flip the bits of its binary representation.

# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero
# bits), and its complement is 010. So you need to output 2.

# Example 2:
# Input: 1
# Output: 0

# Explanation: The binary representation of 1 is 1 (no leading zero
# bits), and its complement is 0. So you need to output 0.

# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.
# This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0: return 1
        significant_bit = 0
        while num >> significant_bit > 0: significant_bit += 1
        mask = 2 ** 31 - 1
        return ~num & ~(mask << significant_bit) & mask

# print("## ", "{0:b}".format(ones))
t = Solution()
print("2 = ", t.findComplement(5))
print("0 = ", t.findComplement(1))
print("1 = ", t.findComplement(0))