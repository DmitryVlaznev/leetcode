# 274. H-Index

# Given an array of citations (each citation is a non-negative integer)
# of a researcher, write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: "A scientist has
# index h if h of his/her N papers have at least h citations each, and
# the other N − h papers have no more than h citations each."

# Example:
# Input: citations = [3,0,6,1,5]
# Output: 3

# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total
#              and each of them had received 3, 0, 6, 1, 5 citations
#              respectively. Since the researcher has 3 papers with at
#              least 3 citations each and the remaining two with no more
#              than 3 citations each, her h-index is 3.

# Note: If there are several possible values for h, the maximum one is
# taken as the h-index.

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ll = len(citations)
        count = [0] * (ll + 1)
        for n in citations:
            count[min(n, ll)] += 1
        at_least = 0
        for h in range(ll, -1, -1):
            at_least += count[h]
            if at_least >= h and ll - at_least <= ll - h:
                return h
        return 0

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