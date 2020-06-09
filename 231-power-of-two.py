# 231. Power of Two

# Given an integer, write a function to determine if it is a power of
# two.

# Example 1:
# Input: 1
# Output: true
# Explanation: 2^0 = 1

# Example 2:
# Input: 16
# Output: true
# Explanation: 2^4 = 16

# Example 3:
# Input: 218
# Output: false

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return not(n & (n - 1))

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(False, t.isPowerOfTwo(0))
log(False, t.isPowerOfTwo(218))
log(True, t.isPowerOfTwo(1))
log(True, t.isPowerOfTwo(16))