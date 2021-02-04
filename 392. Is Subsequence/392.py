class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        p = ''
        for i in range(len(s)):
            while j<len(t):
                if t[j]==s[i]:
                    p+=t[j]
                    j+=1
                    break
                else:
                    j+=1
        if p==s:
            return True
        else:
            return False