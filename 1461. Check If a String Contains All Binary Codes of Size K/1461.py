class Solution:
    def binary(self, i,k):
        ans = ''
        if i ==0:
            return '0'*k
        while i>0:
            ans += str(i%2)
            i = i//2
        if len(ans)<k:
            ans = '0'*(k-len(ans))+ans
        return ans
    def hasAllCodes(self, s: str, k: int) -> bool:
        z = (2**k) - 1
        for i in range(z+1):
            p = self.binary(i,k)
            #print(p)
            if p not in s:
                return False
        return True