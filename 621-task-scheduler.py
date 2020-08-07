# 621. Task Scheduler

# You are given a char array representing tasks CPU need to do. It
# contains capital letters A to Z where each letter represents a
# different task. Tasks could be done without the original order of the
# array. Each task is done in one unit of time. For each unit of time,
# the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the
# cooldown period between two same tasks (the same letter in the array),
# that is that there must be at least n units of time between any two
# same tasks.

# You need to return the least number of units of times that the CPU
# will take to finish all the given tasks.


# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

# Example 2:
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.

# Example 3:
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation:
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A


# Constraints:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].

from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)

        letter_counters = [0] * 26
        for t in tasks: letter_counters[ord(t) - ord('A')] += 1
        letter_counters.sort()
        max_letter = letter_counters.pop()
        empty_slots = (max_letter - 1) * n

        while empty_slots > 0 and letter_counters:
            empty_slots -= min(max_letter - 1, letter_counters.pop())
        empty_slots = max(0, empty_slots)

        return empty_slots + len(tasks)


def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log(8, t.leastInterval(["A","A","A","B","B","B","C","C"], 1))
log(8, t.leastInterval(["A","A","A","B","B","B","C","C"], 0))
log(10, t.leastInterval(["A","A","A","A","B","B","B","C","C","C"], 1))