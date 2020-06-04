# 1029. Two City Scheduling

# There are 2N people a company is planning to interview. The cost of
# flying the i-th person to city A is costs[i][0], and the cost of
# flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that
# exactly N people arrive in each city.

# Example 1:
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation:
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.

# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the
# people interviewing in each city.

# Note:
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = [[abs(p[0] - p[1]), p] for p in costs]
        diffs.sort(reverse=True, key=lambda i: i[0])

        total = fc = sc = 0
        limit = len(costs) // 2
        for d, p in diffs:
            a, b = p
            if fc == limit:
                total += b
                sc += 1
            elif sc == limit:
                total += a
                fc += 1
            elif a < b:
                total += a
                fc += 1
            else:
                total += b
                sc += 1

        return total

def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(110, t.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
log(0, t.twoCitySchedCost([]))
log(20, t.twoCitySchedCost([[10,20]]))
