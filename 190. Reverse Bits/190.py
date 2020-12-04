class Solution:
    def reverseBits(self, n: int) -> int:
        k = str(bin(n))
        k = k.replace('0b','')
        if len(k)<32:
            p = '0'*(32-len(k))
            k = p+ k
        k = k[::-1]
        return int(k,2)