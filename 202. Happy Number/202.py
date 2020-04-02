class Solution:
    def isHappy(self, n: int) -> bool:
        k = str(n)
        if n==1:
            return True
        list = []
        while True:
            p =0 
            for i in k:
                p+=int(i)**2
            k = str(p)
            if p==1:
                return True
            if k not in list:
                list.append(k)
            else:
                return False
        if int(k)==1:
            return True
        else:
            return False
    
        