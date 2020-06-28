# 332. Reconstruct Itinerary

# Given a list of airline tickets represented by pairs of departure and
# arrival airports [from, to], reconstruct the itinerary in order. All
# of the tickets belong to a man who departs from JFK. Thus, the
# itinerary must begin with JFK.

# Note:

# If there are multiple valid itineraries, you should return the
# itinerary that has the smallest lexical order when read as a single
# string. For example, the itinerary ["JFK", "LGA"] has a smaller
# lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.

# Example 1:
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

# Example 2:
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.

from typing import List


class Solution:
    def backtrack(self, path, graph, rest, length):
        if len(path) == length + 1: return path
        src = path[-1]
        # check that it is not a dead end
        if src in graph:
            for dst in graph[src]:
                if rest[src + dst] > 0:
                    rest[src + dst] -= 1
                    path.append(dst)
                    res = self.backtrack(path, graph, rest, length)
                    if res is not None:
                        return res
                    rest[src + dst] += 1
                    path.pop()
        return None

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda t: t[0] + t[1])

        print("tickets =>", tickets)

        rest = {}
        graph = {}
        for src, dst in tickets:
            if src not in graph: graph[src] = []
            if src + dst not in rest:
                graph[src].append(dst)
            if src + dst not in rest: rest[src + dst] = 0
            rest[src + dst] += 1

        path = ["JFK"]
        return self.backtrack(path, graph, rest, len(tickets))


        # print("tickets =>", tickets)
        # print("graph =>", graph)
        # print("rest =>", rest)


t = Solution()
print("----------")
print(["JFK","ATL","JFK","SFO","ATL","SFO"], "<<< correct")
print(t.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print("")

print("----------")
print(t.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(["JFK", "MUC", "LHR", "SFO", "SJC"], "<<< correct")
print("")

print("----------")
print(t.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(["JFK","ATL","JFK","SFO","ATL","SFO"], "<<< correct")
print("")

print("----------")
print(t.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print(["JFK","NRT","JFK","KUL"], "<<< correct")
print("")

print("----------")
print(t.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))
print(["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"], "<<< correct")
print("")

