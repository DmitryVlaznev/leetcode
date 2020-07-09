# 66. Plus One

# Given a non-empty array of digits representing a non-negative integer,
# plus one to the integer.

# The digits are stored such that the most significant digit is at the
# head of the list, and each element in the array contain a single
# digit.

# You may assume the integer does not contain any leading zero, except
# the number 0 itself.

# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + add > 9: digits[i] = 0
            else:
                digits[i] += add
                return digits
        return [1] + digits


def log(correct, res):
    if len(correct) == len(res) and "".join(str(s) for s in correct) == "".join(str(s) for s in res):
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log([1,2,4], t.plusOne([1,2,3]))
log([4,3,2,2], t.plusOne([4,3,2,1]))
log([4,4,0,0], t.plusOne([4,3,9,9]))
log([1,0,0], t.plusOne([9,9]))
log([1], t.plusOne([0]))
log([1,1], t.plusOne([1,0]))
log([2,4,9,4,0], t.plusOne([2,4,9,3,9]))

