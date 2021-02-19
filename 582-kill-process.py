# 582. Kill Process

# Medium

# Given n processes, each process has a unique PID (process id) and its
# PPID (parent process id).

# Each process only has one parent process, but may have one or more
# children processes. This is just like a tree structure. Only one
# process has PPID that is 0, which means this process has no parent
# process. All the PIDs will be distinct positive integers.

# We use two list of integers to represent a list of processes, where
# the first list contains PID for each process and the second list
# contains the corresponding PPID.

# Now given the two lists, and a PID representing a process you want to
# kill, return a list of PIDs of processes that will be killed in the
# end. You should assume that when a process is killed, all its children
# processes will be killed. No order is required for the final answer.

# Example 1:
# Input:
# pid =  [1, 3, 10, 5]
# ppid = [3, 0, 5, 3]
# kill = 5
# Output: [5,10]
# Explanation:
#            3
#          /   \
#         1     5
#              /
#             10
# Kill 5 will also kill 10.
# Note:
# The given kill id is guaranteed to be one of the given PIDs.
# n >= 1.

from typing import List
from collections import deque
from utils import checkList


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = {}
        for i in range(len(pid)):
            if ppid[i] not in tree:
                tree[ppid[i]] = []
            tree[ppid[i]].append(pid[i])

        res, dq = [], deque()
        dq.append(kill)
        while dq:
            l = len(dq)
            while l:
                l -= 1
                process = dq.popleft()
                res.append(process)
                if process in tree:
                    dq.extend(tree[process])
        return res


t = Solution()

checkList([5, 10], t.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5))
