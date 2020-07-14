class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ma = 360/60 * minutes
        ha = 360/12 * hour + minutes/60 * 360/12
        a1 = max(ha, ma) - min(ha, ma)
        a2 = min(ha, ma) + (360 - max(ha, ma)) 
        return min(a1, a2)
