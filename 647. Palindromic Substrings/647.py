class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        for l in range(1,len(s)+1):
            for i in range(len(s)-l+1):
                k = s[i:i+l]
                if k==k[::-1]:
                    c+=1
        return c