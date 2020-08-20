# 416. Partition Equal Subset Sum

# Given a non-empty array containing only positive integers, find if the
# array can be partitioned into two subsets such that the sum of
# elements in both subsets is equal.

# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.

# Example 1:
# Input: [1, 5, 11, 5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].


# Example 2:
# Input: [1, 2, 3, 5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 or len(nums) < 2: return False

        t = s // 2
        complements = [False] * (t + 1)
        complements[0] = True
        for n in nums:
            p = t
            while p - n >= 0:
                if complements[p - n] == True: complements[p] = True
                p -= 1
            if complements[t]: return True
        return False

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log(True, t.canPartition([1, 5, 11, 5]))
log(True, t.canPartition([11, 5, 1, 5]))
log(False, t.canPartition([1, 2, 3, 5]))
log(True, t.canPartition([1, 2, 3, 3, 7]))
log(True, t.canPartition([1, 2, 3, 3, 5]))
log(True, t.canPartition([23,13,11,7,6,5,5]))

