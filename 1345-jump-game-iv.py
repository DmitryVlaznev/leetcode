# 1345. Jump Game IV

# Hard

# Given an array of integers arr, you are initially positioned at the
# first index of the array.

# In one step you can jump from index i to index:

# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the
# array.

# Notice that you can not jump outside of the array at any time.

# Example 1:
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3

# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note
# that index 9 is the last index of the array.

# Example 2:
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You don't need to jump.

# Example 3:
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is
# last index of the array.

# Example 4:
# Input: arr = [6,1,9]
# Output: 2

# Example 5:
# Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
# Output: 3


# Constraints:
# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8

from typing import List
from utils import checkValue


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = {}
        for i, v in enumerate(arr):
            if v not in graph:
                graph[v] = set()
            graph[v].add(i)

        visited, length = set(), 0

        from collections import deque

        dq = deque()
        dq.append(0)
        visited.add(0)
        while dq:
            next_to = len(dq)
            while next_to:
                next_to -= 1
                i = dq.popleft()
                if i == len(arr) - 1:
                    return length

                for sibling in graph[arr[i]]:
                    if sibling not in visited:
                        visited.add(sibling)
                        dq.append(sibling)
                graph[arr[i]] = set()
                if i - 1 >= 0 and i - 1 not in visited:
                    visited.add(i - 1)
                    dq.append(i - 1)
                if i + 1 < len(arr) and i + 1 not in visited:
                    visited.add(i + 1)
                    dq.append(i + 1)
            length += 1


t = Solution()

checkValue(3, t.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
checkValue(0, t.minJumps([7]))
checkValue(1, t.minJumps([7, 6, 9, 6, 9, 6, 9, 7]))
checkValue(2, t.minJumps([6, 1, 9]))
checkValue(3, t.minJumps([11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))
checkValue(2, t.minJumps([7, 7, 7, 7, 7, 7, 7, 11]))
