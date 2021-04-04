# 474. Ones and Zeroes

# Medium

# You are given an array of binary strings strs and two integers m and
# n.

# Return the size of the largest subset of strs such that there are at
# most m 0's and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements
# of y.

# Example 1:
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10",
# "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1",
# "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

# Example 2:
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.

# Constraints:
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100

# https://leetcode.com/problems/ones-and-zeroes/discuss/1138534/Python-short-dp-explained

# Actually, what is asked: let as have k pairs (x1, y1), ... ,(xk, yk).
# We need to answer, how many of them we can choose, so sum of all
# chosen x less than m and sum of all chosen y is less than n.

# One way to solve it is to use dp(mm, nn, kk), where:

# mm is how many zeroes we still allowed to take
# nn is how many ones we still allowed to take
# kk is how many pairs our of k we already processed
# Then what we can do is the following:

# if mm < 0 or nn < 0, we return -float("inf"), because we take more
# zeroes or ones than allowed
# if kk = len(strs), it means, that we out of pairs, return 0.
# finally, we can have two options: either take the last pair or not,
# and we choose the maximum.

# Complexity
# Time and space complexity is O(mnk), where k is number of strings,
# because we have this number of states and only 2 transitions from
# given state.


from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        xy = [[s.count("0"), s.count("1")] for s in strs]

        from functools import cache

        @cache()
        def dp(mm, nn, kk):
            if mm < 0 or nn < 0:
                return -float("inf")
            if kk == len(strs):
                return 0
            x, y = xy[kk]
            return max(1 + dp(mm - x, nn - y, kk + 1), dp(mm, nn, kk + 1))

        return dp(m, n, 0)