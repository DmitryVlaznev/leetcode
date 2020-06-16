# 354. Russian Doll Envelopes

# You have a number of envelopes with widths and heights given as a pair
# of integers (w, h). One envelope can fit into another if and only if
# both the width and height of one envelope is greater than the width
# and height of the other envelope.

# What is the maximum number of envelopes can you Russian doll? (put one
# inside other)

# Note:
# Rotation is not allowed.

# Example:
# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3

# Explanation: The maximum number of envelopes you can Russian doll is 3
# ([2,3] => [5,4] => [6,7]).

from typing import List


class Solution:
    # O(n log n) solution
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 0: return 0

        import functools
        from bisect import bisect_left

        def comparator(a, b):
            if a[0] < b[0]: return -1
            if a[0] > b[0]: return 1
            if a[1] > b[1]: return -1
            if a[1] < b[1]: return 1
            return 0
        envelopes.sort(key=functools.cmp_to_key(comparator))
        heights = [e[1] for e in envelopes]
        dp = []
        for n in heights:
            idx = bisect_left(dp, n)
            if len(dp) == idx: dp.append(n)
            else: dp[idx] = n
        return len(dp)

    # O(n^2) solution
    def maxEnvelopesN2(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) == 0: return 0

        import functools
        from bisect import bisect_left

        def comparator(a, b):
            if a[0] < b[0]: return -1
            if a[0] > b[0]: return 1
            if a[1] < b[1]: return -1
            if a[1] > b[1]: return 1
            return 0

        envelopes.sort(key=functools.cmp_to_key(comparator))
        res = 1
        dp = [1] * len(envelopes)
        for i, n in enumerate(envelopes):
            for j in range(i):
                if n[0] > envelopes[j][0] and n[1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(dp[i], res)
        return res

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(3, t.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
log(1, t.maxEnvelopes([[5,4]]))
log(0, t.maxEnvelopes([]))
log(1, t.maxEnvelopes([[5,40],[16,2]]))
log(4, t.maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))
log(7, t.maxEnvelopes([[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]))


