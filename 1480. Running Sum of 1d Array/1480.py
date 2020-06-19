class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        k=0
        n=[]
        for i in nums:
            k+=i
            n.append(k)
        return n