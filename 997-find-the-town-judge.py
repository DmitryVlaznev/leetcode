# 997. Find the Town Judge

# In a town, there are N people labelled from 1 to N.  There is a rumor
# that one of these people is secretly the town judge.

# If the town judge exists, then:
# * The town judge trusts nobody.
# * Everybody (except for the town judge) trusts the town judge.
# * There is exactly one person that satisfies properties 1 and 2.

# You are given trust, an array of pairs trust[i] = [a, b] representing
# that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of
# the town judge.  Otherwise, return -1.

# Example 1:
# Input: N = 2, trust = [[1,2]]
# Output: 2

# Example 2:
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3:
# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

# Example 4:
# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1

# Example 5:
# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3

# Note:

# 1 <= N <= 1000
# trust.length <= 10000
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N

from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trustMe = [0] * (N + 1)
        trustSomeone = [False] * (N + 1)

        for p in trust:
            trustSomeone[p[0]] = True
            trustMe[p[1]] += 1

        for i in range(1, len(trustSomeone)):
            if trustSomeone[i] == True: continue
            if trustMe[i] == N - 1: return i

        return -1

t = Solution()
print("2 = ", t.findJudge(2, [[1,2]]))
print("3 = ", t.findJudge(3, [[1,3],[2,3]]))
print("4 = ", t.findJudge(4, [[1,3],[2,3],[1,4],[2,4],[3,4]]))
print("-1 = ", t.findJudge(3, [[1,3],[2,3],[3,1]]))
print("-1 = ", t.findJudge(3, [[1,2],[2,3]]))
print("3 = ", t.findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
print("1 = ", t.findJudge(1, []))
print("-1 = ", t.findJudge(2, []))

