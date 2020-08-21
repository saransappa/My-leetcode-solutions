class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        e = []
        o = []
        for i in A:
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        e.extend(o)
        return e