# 957. Prison Cells After N Days

# There are 8 prison cells in a row, and each cell is either occupied or
# vacant.

# Each day, whether the cell is occupied or vacant changes according to
# the following rules:
# * If a cell has two adjacent neighbors that are both occupied or both
#   vacant, then the cell becomes occupied.
# * Otherwise, it becomes vacant.
# * (Note that because the prison is a row, the first and the last cells
#   in the row can't have two adjacent neighbors.)

# We describe the current state of the prison in the following way:
# cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

# Given the initial state of the prison, return the state of the prison
# after N days (and N such changes described above.)


# Example 1:
# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation:
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

# Example 2:
# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]

# Note:
# cells.length == 8
# cells[i] is in {0, 1}
# 1 <= N <= 10^9

from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        def nextDay(cur_day):
            next_day = 0
            mask = 5
            for b in range(1, 7):
                if cur_day & mask == mask or ~cur_day & mask == mask:
                    next_day |= 1 << b
                mask *= 2
            return next_day

        seen = [None] * 256
        cur_day = 0
        for i in range(8):
            if cells[i]: cur_day |= 1 << (7 - i)

        skipped = False
        while N > 0:
            if not skipped and seen[cur_day] is not None:
                d = cur_day
                cycle_length = 1
                while seen[d] != cur_day:
                    cycle_length += 1
                    d = seen[d]
                N = N % cycle_length
                if N > 0: cur_day = seen[cur_day]
                skipped = True
            else:
                next_day = nextDay(cur_day)
                seen[cur_day] = next_day
                cur_day = next_day
            N -= 1

        res = [0,0,0,0,0,0,0,0]
        for i in range(8):
            if cur_day & (1 << i):
                res[7 - i] = 1
        return res

def log(correct, res):
    if len(correct) == len(res) and "".join(str(s) for s in correct) == "".join(str(s) for s in res):
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log([0,0,1,1,1,1,1,0], t.prisonAfterNDays([1,0,0,1,0,0,1,0], 20))
log([0,1,0,0,1,0,0,0], t.prisonAfterNDays([1,0,0,1,0,0,1,0], 50))
log([0,0,1,1,1,1,1,0], t.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))
log([0, 1, 1, 0, 0, 0, 0, 0], t.prisonAfterNDays([0,1,0,1,1,0,0,1], 1))
log([0, 0, 0, 0, 1, 1, 1, 0], t.prisonAfterNDays([0,1,0,1,1,0,0,1], 2))
log([0, 1, 1, 0, 0, 1, 0, 0], t.prisonAfterNDays([0,1,0,1,1,0,0,1], 3))
log([0, 0, 0, 0, 0, 1, 0, 0], t.prisonAfterNDays([0,1,0,1,1,0,0,1], 4))
log([0, 1, 1, 1, 0, 1, 0, 0], t.prisonAfterNDays([0,1,0,1,1,0,0,1], 5))
log([0, 0, 1, 0, 1, 1, 0, 0], t.prisonAfterNDays([0,1,0,1,1,0,0,1], 6))
log([0, 0, 1, 1, 0, 0, 0, 0], t.prisonAfterNDays([0,1,0,1,1,0,0,1], 7))
log([0,0,1,0,1,0,0,0], t.prisonAfterNDays([1,0,0,0,1,0,0,1], 99))

