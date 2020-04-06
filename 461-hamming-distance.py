# 461. Hamming Distance

# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are
# different.

from typing import List


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        res = 0
        while xor > 0:
            if xor & 1: res += 1
            xor = xor >> 1
        return res

t = Solution()

print("2 = ", t.hammingDistance(1, 4))
print("1 = ", t.hammingDistance(1, 5))
print("3 = ", t.hammingDistance(15, 1))