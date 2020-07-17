class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        k = log2(n)
        if k == int(k):
            return True
        else:
            return False