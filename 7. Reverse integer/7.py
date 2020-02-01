class Solution:
    def reverse(self, x: int) -> int:
        k=str(x)
        flag=0
        if k[0]=='-':
            k=k.replace('-','')
            flag=1
        p=k[::-1]
        if flag==1:
            p='-'+p
        s=int(p)
        if s<-2**31 or s>2**31-1:
            return 0
        else:
            return s