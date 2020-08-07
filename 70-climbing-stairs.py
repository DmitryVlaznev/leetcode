# 70. Climbing Stairs

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways
# can you climb to the top?

# Example 1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:

# 1 <= n <= 45

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        dp_prev = 1
        dp_last = 2
        for i in range(3, n + 1):
            dp_prev, dp_last = dp_last, dp_prev + dp_last
        return dp_last

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(1, t.climbStairs(1))
log(2, t.climbStairs(2))
log(3, t.climbStairs(3))
log(5, t.climbStairs(4))
log(8, t.climbStairs(5))
log(13, t.climbStairs(6))