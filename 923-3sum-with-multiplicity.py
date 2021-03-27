# 923. 3Sum With Multiplicity

# Medium

# Given an integer array arr, and an integer target, return the number
# of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] ==
# target.

# As the answer can be very large, return it modulo 109 + 7.

# Example 1:
# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation:
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.

# Example 2:
# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation:
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.

# Constraints:
# 3 <= arr.length <= 3000
# 0 <= arr[i] <= 100
# 0 <= target <= 300

from typing import List
from utils import checkValue


class Solution:
    def threeSumMulti(self, arr, target):
        res = 0
        arr.sort()

        for i in range(0, len(arr)):
            rest = target - arr[i]
            j, k = i + 1, len(arr) - 1
            while j < k:
                if arr[j] + arr[k] < rest:
                    j += 1
                elif arr[j] + arr[k] > rest:
                    k -= 1
                elif arr[j] != arr[k]:
                    left = right = 1
                    while j + 1 < k and arr[j] == arr[j + 1]:
                        left, j = left + 1, j + 1
                    while k - 1 > j and arr[k] == arr[k - 1]:
                        right, k = right + 1, k - 1
                    res += left * right
                    res %= 10 ** 9 + 7
                    j, k = j + 1, k - 1
                else:
                    res += (k - j + 1) * (k - j) / 2
                    res %= 10 ** 9 + 7
                    break
        return int(res)

    def threeSumMulti_TLE(self, arr: List[int], target: int) -> int:
        twoSums = {}
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] not in twoSums:
                    twoSums[arr[i] + arr[j]] = []
                twoSums[arr[i] + arr[j]].append((i, j))
        res = 0
        for n in range(2, len(arr)):
            rest = target - arr[n]
            if rest in twoSums:
                pairs = twoSums[rest]
                for i, j in pairs:
                    if n > i and n > j:
                        res += 1
        return res


t = Solution()
checkValue(20, t.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))
checkValue(12, t.threeSumMulti([1, 1, 2, 2, 2, 2], 5))