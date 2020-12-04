class Solution:
    def hammingWeight(self, n: int) -> int:
        k = bin(n)
        return k.count('1')