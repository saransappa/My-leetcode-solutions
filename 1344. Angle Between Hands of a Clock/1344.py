class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        k = abs((11/2)*minutes - 30*hour)
        return min(k,360-k)