class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n *= -1
        res = 1
        mul = x
        while n > 0:
            if n % 2: res = res * mul
            mul = mul * mul
            n = n // 2
        return res
