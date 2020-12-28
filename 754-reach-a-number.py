# 754. Reach a Number

# Medium

# You are standing at position 0 on an infinite number line. There is a
# goal at position target.

# On each move, you can either go left or right. During the n-th move
# (starting from 1), you take n steps.

# Return the minimum number of steps required to reach the destination.

# Example 1:
# Input: target = 3
# Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.

# Example 2:
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.

# Note:
# target will be a non-zero integer in the range [-10^9, 10^9].

from utils import checkValue


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        # S = n(n+1)/2 => n = (2*S + 1) ** 0.5 - 1
        # for n = 44721 S > 10**9

        # find the closest n when Sn <= target
        l, r = 0, 44721
        while r - l > 1:
            mid = l + (r - l) // 2
            S = mid * (mid + 1) // 2
            if S < target:
                l = mid
            else:
                r = mid

        s, step = r * (r + 1) // 2, r
        while (s - target) % 2 != 0:
            step = step + 1
            s = s + step
        return step


t = Solution()
checkValue(2, t.reachNumber(3))
checkValue(3, t.reachNumber(2))
checkValue(11, t.reachNumber(42))