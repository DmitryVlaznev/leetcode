# 441. Arranging Coins

# You have a total of n coins that you want to form in a staircase
# shape, where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be
# formed.

# n is a non-negative integer and fits within the range of a 32-bit
# signed integer.

# Example 1:
# n = 5
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# Because the 3rd row is incomplete, we return 2.

# Example 2:
# n = 8
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# Because the 4th row is incomplete, we return 3.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 2: return n
        l, r = -1, n
        while r - l > 1:
            mid = l + (r - l) // 2
            if mid * (mid + 1) / 2 <= n: l = mid
            else: r = mid
        return l

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log(2, t.arrangeCoins(5))
log(3, t.arrangeCoins(8))
log(1, t.arrangeCoins(1))
log(0, t.arrangeCoins(0))
log(2, t.arrangeCoins(3))
log(4, t.arrangeCoins(10))
log(2, t.arrangeCoins(4))