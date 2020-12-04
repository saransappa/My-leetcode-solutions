class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        k = []
        for i in nums:
            if nums.count(i)==1:
                k.append(i)
        return k