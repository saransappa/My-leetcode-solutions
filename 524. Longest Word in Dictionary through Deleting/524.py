class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        z = []
        for w in d:
            i = 0
            j = 0
            k = ''
            while i<len(s) and j<len(w):
                if s[i]==w[j]:
                    k+=s[i]
                    i+=1
                    j+=1
                else:
                    i+=1
            if k in d:
                z.append(k)
        z.sort(key=lambda x: (-len(x),x))
        for i in z:
            print(i,len(i))
        if len(z)==0:
            return ""
        return z[0]