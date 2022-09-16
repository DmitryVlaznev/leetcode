# 967. Numbers With Same Consecutive Differences

# Medium

# Return all non-negative integers of length n such that the absolute
# difference between every two consecutive digits is k.

# Note that every number in the answer must not have leading zeros. For
# example, 01 has one leading zero and is invalid.

# You may return the answer in any order.

# Example 1:
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.

# Example 2:
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


# Constraints:
# 2 <= n <= 9
# 0 <= k <= 9

from typing import List, Tuple
from functools import lru_cache


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def get_diff(digit, k):
            res = []
            for i in range(0, 10):
                if abs(digit - i) == k:
                    res.append(i)
            return tuple(res)

        @lru_cache(maxsize=None)
        def dp(n: int, k: int, start: Tuple[int]):
            if n == 1:
                return [[i] for i in start]
            res = []
            for nxt in start:
                rest = dp(n - 1, k, get_diff(nxt, k))
                for num in rest:
                    if len(num) == n - 1:
                        res.append([nxt] + num)
            return res

        res = []
        digits = dp(n, k, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
        for num in digits:
            if num[0] != 0:
                res.append(int("".join([str(d) for d in num])))
        return res


s = Solution()
s.numsSameConsecDiff(3, 7)
s.numsSameConsecDiff(2, 1)
