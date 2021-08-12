# 954. Array of Doubled Pairs

# Medium

# Given an array of integers arr of even length, return true if and only
# if it is possible to reorder it such that arr[2 * i + 1] = 2 * arr[2 *
# i] for every 0 <= i < len(arr) / 2.

# Example 1:
# Input: arr = [3,1,3,6]
# Output: false

# Example 2:
# Input: arr = [2,1,2,6]
# Output: false

# Example 3:
# Input: arr = [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form
# [-2,-4,2,4] or [2,4,-2,-4].

# Example 4:
# Input: arr = [1,2,4,16,8,4]
# Output: false


# Constraints:
# 0 <= arr.length <= 3 * 10^4
# arr.length is even.
# -10^5 <= arr[i] <= 10^5

from typing import List
from utils import checkValue


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        def check(a: List[int]):
            if not a:
                return True
            if len(a) % 2:
                return False
            res = [None] * len(a)
            a.sort()
            p_base, p_empty = 0, 2
            for n in a:
                if res[p_base] is None:
                    res[p_base] = n
                    continue
                if res[p_base] * 2 == n:
                    res[p_base + 1] = n
                    p_base += 2
                    p_empty = p_empty if p_empty > p_base else p_base + 2
                    continue
                if res[p_base] * 2 < n:
                    return False
                if p_empty >= len(a):
                    return False
                res[p_empty] = n
                p_empty += 2
            return True

        zeroes, positive, negative = 0, [], []
        for n in arr:
            if n < 0:
                negative.append(-1 * n)
            elif n > 0:
                positive.append(n)
            else:
                zeroes += 1
        if zeroes % 2:
            return False
        return check(positive) and check(negative)


s = Solution()

checkValue(False, s.canReorderDoubled([3, 1, 3, 6]))
checkValue(False, s.canReorderDoubled([2, 1, 2, 6]))
checkValue(True, s.canReorderDoubled([4, -2, 2, -4]))
checkValue(False, s.canReorderDoubled([1, 2, 4, 16, 8, 4]))

checkValue(False, s.canReorderDoubled([10, 12, 15, 20, 21, 24, 30]))
checkValue(True, s.canReorderDoubled([10, 12, 15, 20, 24, 30]))
