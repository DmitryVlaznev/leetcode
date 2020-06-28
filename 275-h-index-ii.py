# 275. H-Index II

# Given an array of citations sorted in ascending order (each citation
# is a non-negative integer) of a researcher, write a function to
# compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has
# index h if h of his/her N papers have at least h citations each, and
# the other N − h papers have no more than h citations each."

# Example:
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total
#              and each of them had received 0, 1, 3, 5, 6 citations
#              respectively. Since the researcher has 3 papers with at
#              least 3 citations each and the remaining two with no more
#              than 3 citations each, her h-index is 3.

# Note:
# If there are several possible values for h, the maximum one is taken
# as the h-index.

# Follow up:
# This is a follow up problem to H-Index, where citations is now
# guaranteed to be sorted in ascending order.
# Could you solve it in logarithmic time complexity?

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        n = len(citations)
        l, r = -1, n
        while r - l > 1:
            mid = l + ((r - l) // 2)
            h = citations[mid]
            if h >= n - mid : r = mid
            else: l = mid
        return n - r

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(3, t.hIndex([0,1,3,5,6]))
log(1, t.hIndex([0,1,1,1,2]))
log(3, t.hIndex([0,1,4,5,6]))
log(1, t.hIndex([0,0,5]))
log(2, t.hIndex([0,1,2,5,6]))
log(4, t.hIndex([4,4,4,8,8]))
log(6, t.hIndex([2,10,11,12,13,14,15]))
log(1, t.hIndex([2]))
log(0, t.hIndex([0]))
log(0, t.hIndex([]))