# 264. Ugly Number II
# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2,
# 3, 5.

# Example:

# Input: n = 10
# Output: 12

# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the
# first 10 ugly numbers.

# Note:
# 1 is typically treated as an ugly number.
# n does not exceed 1690.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        h = []
        num = None
        heapq.heappush(h, 1)
        seen = set()
        seen.add(1)
        while n > 0:
            num = heapq.heappop(h)
            if num * 2 not in seen:
                heapq.heappush(h, num * 2)
                seen.add(num * 2)
            if num * 3 not in seen:
                heapq.heappush(h, num * 3)
                seen.add(num * 3)
            if num * 5 not in seen:
                heapq.heappush(h, num * 5)
                seen.add(num * 5)
            n -= 1
        return num

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log(1, t.nthUglyNumber(1))
log(5, t.nthUglyNumber(5))
log(12, t.nthUglyNumber(10))
log(2123366400, t.nthUglyNumber(1690))
