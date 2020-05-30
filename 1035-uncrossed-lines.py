# 1035. Uncrossed Lines

# We write the integers of A and B (in the order they are given) on two
# separate horizontal lines.

# Now, we may draw connecting lines: a straight line connecting two
# numbers A[i] and B[j] such that: A[i] == B[j];

# The line we draw does not intersect any other connecting
# (non-horizontal) line. Note that a connecting lines cannot intersect
# even at the endpoints: each number can only belong to one connecting
# line.
# Return the maximum number of connecting lines we can draw in this way.

# Example 1:
# Input: A = [1,4,2], B = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

# Example 2:
# Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
# Output: 3

# Example 3:
# Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
# Output: 2

# Note:
# 1 <= A.length <= 500
# 1 <= B.length <= 500
# 1 <= A[i], B[i] <= 2000

from typing import List

## Basic Ideas: dynamic programming
## Basic Ideas: dynamic programming
##
##  Each time we need to draw a line from one tailing node
##    dp from left to right
##
##   dp(i, j): the result of A[:i] and B[:j]
##       dp(i-1, j), dp(i, j-1)
##         Need to check whether A[i] == B[j]
##
##       If A[i] != B[j]
##           dp(i, j) = max(dp(i-1, j), dp(i, j-1))
##
##       If A[i] == B[j]
##           draw a line between A[i] and B[j]
##           dp(i, j) = max(1 + dp(i-1, j-1), previous case)
##
## Complexity: Time O(n*m), Space O(n*m)
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for i in range(len(A) + 1)]

        res = 0
        for i in range(1, len(dp)):
            for j in range (1, len(dp[0])):
                dp[i][j]= max(dp[i-1][j], dp[i][j-1])
                if A[i-1] == B[j-1]:
                    dp[i][j] = max(dp[i][j], 1+dp[i-1][j-1])
                res = max(res, dp[i][j])
        return res



def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(2, t.maxUncrossedLines([1,4,2], [1,2,4]))
log(3, t.maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]))
log(2, t.maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1]))
log(0, t.maxUncrossedLines([43], [1,9,2,5,1]))
log(0, t.maxUncrossedLines([1,3,7,1,7,5], [42]))
log(2, t.maxUncrossedLines([2,1], [1,2,1,3,3,2]))
log(1, t.maxUncrossedLines([3], [3,3,2]))



