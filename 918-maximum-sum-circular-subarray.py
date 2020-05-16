# 918. Maximum Sum Circular Subarray

# Given a circular array C of integers represented by A, find the
# maximum possible sum of a non-empty subarray of C.

# Here, a circular array means the end of the array connects to the
# beginning of the array.  (Formally, C[i] = A[i] when 0 <= i <
# A.length, and C[i+A.length] = C[i] when i >= 0.)

# Also, a subarray may only include each element of the fixed buffer A
# at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j],
# there does not exist i <= k1, k2 <= j with k1 % A.length = k2 %
# A.length.)

# Example 1:
# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3

# Example 2:
# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

# Example 3:
# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

# Example 4:
# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

# Example 5:
# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1

# Note:
# -30000 <= A[i] <= 30000
# 1 <= A.length <= 30000

from typing import List


class Solution:
    def kadane(self, arr: List[int]) -> int:
        l = len(arr)
        curSeqSum, seqSum = float("-inf"), float("-inf")
        p = 0
        while p < l:
            curSeqSum = arr[p] if curSeqSum <= 0 else curSeqSum + arr[p]
            seqSum = max(curSeqSum, seqSum)
            p += 1
        return seqSum

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        k_max = self.kadane(A)
        if k_max < 0: return k_max
        sum_all = 0
        for i in range(0, len(A)):
            sum_all += A[i]
            A[i] = -A[i]
        k_min = -self.kadane(A)
        return k_max if k_max > (sum_all - k_min) else (sum_all - k_min)

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(3, t.maxSubarraySumCircular([1,-2,3,-2]))
log(3, t.maxSubarraySumCircular([3,-2,2,-3]))
log(-1, t.maxSubarraySumCircular([-2,-3,-1]))
log(-1, t.maxSubarraySumCircular([-3,-2,-1]))
log(-1, t.maxSubarraySumCircular([-1,-2,-3]))
log(22, t.maxSubarraySumCircular([5,2,-3,10,-10,-15,21,-50,5,-1,2,-1,3]))
log(4, t.maxSubarraySumCircular([3,-1,2,-1]))
log(6, t.maxSubarraySumCircular([1,2,3]))
log(6, t.maxSubarraySumCircular([3,2,1]))
log(-2, t.maxSubarraySumCircular([-13,-2,-3]))
log(10, t.maxSubarraySumCircular([5,-3,5]))

arr = [88,-35,50,-38,-60,-31,-2,-8,-8,91,-14,50,-25,-26,1,71,-91,-64,-40,46,30,-97,9,-55,-36,-75,71,99,90,-53,-68,-20,-73,89,-14,74,-8,72,82,48,45,2,-42,12,77,22,87,56,73,-21,78,15,-6,-75,24,46,-11,-70,-90,-77,57,43,-66,10,-30,-47,91,-37,-4,-67,-88,19,66,29,86,97,-4,67,54,-92,-54,71,-42,-17,57,-91,-9,-15,-26,56,-57,-58,-72,91,-55,35,-20,29,51,70]
log(810, t.maxSubarraySumCircular(arr))