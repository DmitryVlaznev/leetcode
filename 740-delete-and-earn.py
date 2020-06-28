# 740. Delete and Earn

# Given an array nums of integers, you can perform operations on the
# array.

# In each operation, you pick any nums[i] and delete it to earn nums[i]
# points. After, you must delete every element equal to nums[i] - 1 or
# nums[i] + 1.

# You start with 0 points. Return the maximum number of points you can
# earn by applying such operations.

# Example 1:
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation:
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.

# Example 2:
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation:
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.


# Note:
# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            if k - 1 != prev:
                m = max(avoid, using)
                using = k * count[k] + m
                avoid = m
            else:
                m = max(avoid, using)
                using = k * count[k] + avoid
                avoid = m
            prev = k
        return max(avoid, using)

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

# log(6, t.deleteAndEarn([3, 4, 2]))
# log(9, t.deleteAndEarn([2, 2, 3, 3, 3, 4]))
log(12, t.deleteAndEarn([2, 2, 2, 3, 4, 4, 4, 5, 6]))