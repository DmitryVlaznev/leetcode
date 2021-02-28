# 946. Validate Stack Sequences

# Medium

# Given two sequences pushed and popped with distinct values, return
# true if and only if this could have been the result of a sequence of
# push and pop operations on an initially empty stack.

# Example 1:
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

# Example 2:
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.

# Constraints:
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.

from typing import List
from utils import checkValue


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, p, q = [], 0, 0
        while p <= len(pushed) and q < len(popped):
            if stack and stack[-1] == popped[q]:
                stack.pop()
                q += 1
            elif not stack or stack[-1] != popped[q]:
                if p == len(pushed):
                    return False
                stack.append(pushed[p])
                p += 1
        return q == len(popped)


t = Solution()

checkValue(True, t.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
checkValue(False, t.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
checkValue(True, t.validateStackSequences([1], [1]))
checkValue(False, t.validateStackSequences([1], [2]))
checkValue(True, t.validateStackSequences([], []))
