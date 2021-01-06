# 526. Beautiful Arrangement

# Medium

# Suppose you have n integers start 1 to n. We define a beautiful
# arrangement as an array that is constructed by these n numbers
# successfully if one of the following is true for the ith position (1
# <= i <= n) in this array:

# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# Given an integer n, return the number of the beautiful arrangements
# that you can construct.

# Example 1:
# Input: n = 2
# Output: 2
# Explanation:
# The first beautiful arrangement is [1, 2]:
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
# The second beautiful arrangement is [2, 1]:
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

# Example 2:
# Input: n = 1
# Output: 1

# Constraints:
# 1 <= n <= 15

from typing import Set, List
from utils import checkValue


class Solution:
    res = 0

    def makeArrangement(self, start, rest_numbers: Set[int]):
        if not rest_numbers:
            self.res += 1
            return
        for n in rest_numbers:
            if n % start == 0 or start % n == 0:
                next_numbers = rest_numbers.copy()
                next_numbers.remove(n)
                self.makeArrangement(start + 1, next_numbers)

    def countArrangement(self, n: int) -> int:
        self.res = 0
        self.makeArrangement(1, set([i for i in range(1, n + 1)]))
        return self.res


# class Solution:
#     res = 0
#     sets = []

#     def makeArrangement(self, start, rest_numbers: Set[int], cur_set: List[int]):
#         if not rest_numbers:
#             self.res += 1
#             self.sets.append(cur_set)
#             return
#         for n in rest_numbers:
#             if n % start == 0 or start % n == 0:
#                 next_numbers = rest_numbers.copy()
#                 next_numbers.remove(n)
#                 self.makeArrangement(start + 1, next_numbers, cur_set + [n])

#     def countArrangement(self, n: int) -> int:
#         self.res = 0
#         self.makeArrangement(1, set([i for i in range(1, n + 1)]), [])
#         print(self.sets)
#         return self.res

t = Solution()

checkValue(2, t.countArrangement(2))
checkValue(1, t.countArrangement(1))
checkValue(3, t.countArrangement(3))