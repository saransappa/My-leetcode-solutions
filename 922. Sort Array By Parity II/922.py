class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        e = []
        o = []
        for i in A:
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        ans = []
        for i in range(len(A)):
            if i%2!=0:
                ans.append(o[i//2])
            else:
                ans.append(e[i//2])
        return ans