# 204. Count Primes

# Easy

# Count the number of prime numbers less than a non-negative number, n.

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5,
# 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0

# Constraints:
# 0 <= n <= 5 * 10^6

from utils import checkValue


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        sieve = [i for i in range(3, n, 2)]
        for p in sieve:
            if p == -1:
                continue
            q = p ** 2
            while q < n:
                if q % 2 != 0:
                    sieve[(q - 3) // 2] = -1
                q += p
        res = 0
        for p in sieve:
            res += 0 if p == -1 else 1
        return res + 1


t = Solution()


checkValue(0, t.countPrimes(0))
checkValue(0, t.countPrimes(1))
checkValue(0, t.countPrimes(2))
checkValue(4, t.countPrimes(10))
checkValue(4730, t.countPrimes(45644))