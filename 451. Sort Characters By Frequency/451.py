class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if d.get(i,0)==0:
                d[i]=1
            else:
                d[i]+=1
        l = []
        for i in d:
            p = []
            p.append(d[i])
            p.append(i)
            l.append(p)
        l.sort(reverse=True)
        t = ''
        for i in l:
            t+= i[1]*i[0]
        return t