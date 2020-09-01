class Solution:
    def defangIPaddr(self, address: str) -> str:
        k = ''
        s= address
        for i in range(len(s)-1):
            if s[i]!='.':
                k+=s[i]
            if s[i+1]==".":
                k+='[.]'
                i+=1
        return k+s[len(s)-1]