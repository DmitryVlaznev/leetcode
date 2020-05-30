# 338. Counting Bits

# Given a non negative integer number num. For every numbers i in the
# range 0 ≤ i ≤ num calculate the number of 1's in their binary
# representation and return them as an array.

# Example 1:

# Input: 2
# Output: [0,1,1]
# Example 2:

# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:

# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly
# in a single pass?

# Space complexity should be O(n).

# Can you do it like a boss? Do it without using any builtin function
# like __builtin_popcount in c++ or in any other language.

from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        pattern, dp = [0, 1, 1, 2], [0] * (num + 1)
        for n in range(num + 1):
            if n < 4: dp[n] = pattern[n]
            else: dp[n] = dp[n % 4] + dp[n // 4]
        return dp

# print("dp ", dp)
# print("n =", n, "dp[n % 4]", dp[n % 4], "dp[n // 4]", dp[n // 4])
def log(correct, res):
    if len(correct) != len(res): print(">>> INCORRECT >>>", correct, " | ", res)
    for i, n in enumerate(correct):
        if n != res[i]:
            print(">>> INCORRECT >>>", correct, " | ", res)
            return
    print("[v]", res)

t = Solution()

log([0,1,1], t.countBits(2))
log([0,1,1,2,1,2], t.countBits(5))
log([0], t.countBits(0))
log([0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4], t.countBits(23))