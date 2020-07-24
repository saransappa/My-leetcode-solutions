class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        list = []
        list.append(str(x)+' '+str(y))
        for i in path:
            if i=="N":
                y+=1
            elif i=="S":
                y-=1
            elif i=="E":
                x+=1
            else:
                x-=1
            z = str(x)+' '+str(y)
            if z in list:
                return True
            list.append(z)
        return False