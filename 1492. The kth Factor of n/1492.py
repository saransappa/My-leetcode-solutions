class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        z = []
        for i in range(1,n+1):
            if n%i==0:
                z.append(i)
        if len(z)<k:
            return -1
        else:
            return z[k-1]