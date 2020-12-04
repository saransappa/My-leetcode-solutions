class Solution:
    def addBinary(self, a: str, b: str) -> str:
        k = int(a,2)+int(b,2)
        return bin(k)[2:]