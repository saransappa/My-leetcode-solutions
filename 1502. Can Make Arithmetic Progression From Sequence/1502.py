class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        k = []
        arr.sort()
        for i in range(1,len(arr)):
            k.append(arr[i]-arr[i-1])
        z = list(set(k))
        if len(z)==1:
            return True
        else:
            return False