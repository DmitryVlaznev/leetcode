# 1354. Construct Target Array With Multiple Sums

# Hard

# Given an array of integers target. From a starting array, A consisting
# of all 1's, you may perform the following procedure :

# let x be the sum of all elements currently in your array. choose index
# i, such that 0 <= i < target.size and set the value of A at index i to
# x.
# You may repeat this procedure as many times as needed.
# Return True if it is possible to construct the target array from A
# otherwise return False.

# Example 1:
# Input: target = [9,3,5]
# Output: true
# Explanation: Start with [1, 1, 1]
# [1, 1, 1], sum = 3 choose index 1
# [1, 3, 1], sum = 5 choose index 2
# [1, 3, 5], sum = 9 choose index 0
# [9, 3, 5] Done

# Example 2:
# Input: target = [1,1,1,2]
# Output: false
# Explanation: Impossible to create target array from [1,1,1,1].

# Example 3:
# Input: target = [8,5]
# Output: true

# Constraints:
# N == target.length
# 1 <= target.length <= 5 * 10^4
# 1 <= target[i] <= 10^9

from typing import List
import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        s, h = 0, []
        for n in target:
            s += n
            h.append(-n)
        heapq.heapify(h)
        while True:
            n = -heapq.heappop(h)
            if n == 1:
                return True
            if s == n:
                return False
            c = (n - 1) % (s - n) + 1
            if c == n:
                return False
            heapq.heappush(h, -c)
            s = s - n + c
        return True

        heap = []
        for num in target:
            heappush(heap, -num)
        s = sum(target)
        while True:
            elem = -heappop(heap)
            if elem == 1:
                return True
            if s == elem:
                return False
            cand = (elem - 1) % (s - elem) + 1
            if cand == elem:
                return False
            s = s - elem + cand
            heappush(heap, -cand)