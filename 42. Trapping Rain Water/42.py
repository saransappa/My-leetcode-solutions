class Solution:
    def trap(self, height: List[int]) -> int:
        w = height
        while len(w)>0 and w[0]==0:
            w = w[1:]
            w = w[::-1]
        while len(w)>0 and w[0]==0:
            w = w[1:]
        w = w[::-1]
        total = 0
        q = []
        for i in range(len(w)):
            #print('i=',i)
            k = w[i]
            m = i
            l = None
            r = None
            for j in range(i+1,len(w)):
                if w[j]>k:
                    l = w[j]
                    r = j
                    break
            p = l
            a = []
            if l == None:
                for h in range(m+1,len(w)):
                    a.append(w[h])
                a.sort()
                for h in range(m+1,len(w)):
                    if w[h]==a[-1]:
                        r = h
                        break
            if a!=[]:
                p = a[-1]
            if p==None:
                p = w[-1]
                r = len(w)-1
            #print('total=',total)
            z = min(p,k)
            #print(z)
            for s in range(i+1,r):
                if s not in q:
                    q.append(s)
                    #print(z-w[s])
                    total += (z-w[s]) 
                #print('i=',i)
            i = r
        return total