# 67. Add Binary

# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


# Constraints:

# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # arr_a = [int(c) for c in a]
        # arr_b = [int(c) for c in b]
        # print(arr_a)
        # print(arr_b)
            # print(f"pa = {pa}, pb = {pb}")
            # print(f"a = {arr_a[pa]}, b = {arr_b[pb]}, c = {c}")
            # print(f">>> d = {d}, c = {c}, res = {res}")
        pa = len(a) -1
        pb = len(b) -1
        res = []
        c = 0
        d = 0
        while pa >= 0 or pb >= 0:
            if pa >= 0 and pb >= 0:
                d = int(a[pa]) + int(b[pb]) + c
                pa -= 1
                pb -= 1
            elif pa >= 0:
                d = int(a[pa]) + c
                pa -= 1
            elif pb >= 0:
                d = int(b[pb]) + c
                pb -= 1

            if d == 3:
                res.append(1)
                c = 1
            elif d == 2:
                res.append(0)
                c = 1
            else:
                res.append(d)
                c = 0
        if c == 1: res.append(1)
        res.reverse()
        return "".join([str(n) for n in res])

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

t = Solution()

log("10101", t.addBinary("1010", "1011"))
log("100", t.addBinary("11", "1"))
log("1", t.addBinary("1", "0"))
log("0", t.addBinary("0", "0"))
log("11110", t.addBinary("1111", "1111"))