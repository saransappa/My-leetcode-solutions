class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for i in A:
            k = []
            for j in i:
                if j==0:
                    k.append(1)
                else:
                    k.append(0)
            res.append(k[::-1])
        return res